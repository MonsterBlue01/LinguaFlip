import torch
from torch.utils.data import DataLoader, Dataset
from transformers import MarianMTModel, MarianTokenizer, AdamW
from transformers import get_scheduler
from tqdm import tqdm
from pathlib import Path
import os
from torch.cuda.amp import GradScaler, autocast  # Import mixed precision modules

class TranslationDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        if not self.data_dir.exists():
            raise FileNotFoundError(f"The directory {self.data_dir} does not exist.")
        
        self.data_files = sorted(self.data_dir.glob("combined_chunk_*.pt"))
        
        if not self.data_files:
            raise ValueError(f"No .pt files found in {self.data_dir}. Please ensure the tokenization process was successful.")
        
        # Create index mapping
        self.cumulative_lengths = []
        total = 0
        for file in self.data_files:
            data = torch.load(file, map_location='cpu')  # Load using CPU to reduce GPU memory usage
            num_samples = data["src"].size(0)
            total += num_samples
            self.cumulative_lengths.append(total)
        
        self.total_samples = total
        self.current_file = None
        self.current_data = None

        print(f"Total samples in dataset: {self.total_samples}")

    def __len__(self):
        return self.total_samples

    def __getitem__(self, idx):
        import bisect
        file_idx = bisect.bisect_right(self.cumulative_lengths, idx)
        
        if file_idx == 0:
            sample_idx = idx
        else:
            sample_idx = idx - self.cumulative_lengths[file_idx - 1]
        
        # If the current file is not the target file, load the new file
        if self.current_file != self.data_files[file_idx]:
            self.current_file = self.data_files[file_idx]
            self.current_data = torch.load(self.current_file, map_location='cpu')
        
        src = self.current_data["src"][sample_idx]
        tgt = self.current_data["tgt"][sample_idx]
        
        return src, tgt

def train_loop(model, dataloader, optimizer, scheduler, device, scaler, accumulation_steps=1):
    model.train()
    total_loss = 0

    optimizer.zero_grad()

    for i, batch in enumerate(tqdm(dataloader, desc="Training")):
        src, tgt = batch
        src, tgt = src.to(device), tgt.to(device)

        with autocast():
            outputs = model(input_ids=src, labels=tgt)
            loss = outputs.loss / accumulation_steps  # Normalize loss for gradient accumulation

        scaler.scale(loss).backward()

        if (i + 1) % accumulation_steps == 0:
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad()
            scheduler.step()

        total_loss += loss.item() * accumulation_steps  # Multiply back to get the actual loss

    # Handle the last batch if it wasn't a multiple of accumulation_steps
    if len(dataloader) % accumulation_steps != 0:
        scaler.step(optimizer)
        scaler.update()
        optimizer.zero_grad()

    avg_loss = total_loss / len(dataloader)
    print(f"Training Loss: {avg_loss}")
    return avg_loss

def validate_loop(model, dataloader, device):
    model.eval()
    total_loss = 0

    with torch.no_grad():
        for batch in tqdm(dataloader, desc="Validation"):
            src, tgt = batch
            src, tgt = src.to(device), tgt.to(device)

            with autocast():
                outputs = model(input_ids=src, labels=tgt)
                loss = outputs.loss
                total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    print(f"Validation Loss: {avg_loss}")
    return avg_loss

if __name__ == "__main__":
    from pathlib import Path

    try:
        # Get the script path
        script_path = Path(__file__).resolve()
        script_dir = script_path.parent

        # Data and output directories
        data_dir = (script_dir / "../data/processed/tokenized").resolve()
        output_dir = (script_dir / "../outputs/checkpoints").resolve()

        # Print debug information
        print(f"Data directory path: {data_dir}")
        print(f"Output directory path: {output_dir}")

        # Hyperparameters
        num_epochs = 3
        batch_size = 8  # Adjust based on your requirements
        learning_rate = 5e-5
        model_name = "Helsinki-NLP/opus-mt-en-es"

        # Device setup
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"The equipment used is: {device}")

        # Load model and tokenizer
        print("Loading the model and tokenizer...")
        model = MarianMTModel.from_pretrained(model_name).to(device)
        tokenizer = MarianTokenizer.from_pretrained(model_name)

        # Prepare dataset and data loader
        print("Preparing dataset and data loader...")
        dataset = TranslationDataset(data_dir)
        dataloader = DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=True,
            num_workers=1,
            pin_memory=True,
        )

        # Optimizer and scheduler
        optimizer = AdamW(model.parameters(), lr=learning_rate)
        num_training_steps = len(dataloader) * num_epochs
        scheduler = get_scheduler(
            "linear",
            optimizer=optimizer,
            num_warmup_steps=0,
            num_training_steps=num_training_steps
        )

        # Initialize GradScaler
        scaler = GradScaler()

        # Set gradient accumulation steps
        accumulation_steps = 1  # Adjust based on your memory and needs, e.g., 4

        # Training loop
        for epoch in range(num_epochs):
            print(f"\nEpoch {epoch + 1}/{num_epochs}")
            train_loss = train_loop(model, dataloader, optimizer, scheduler, device, scaler, accumulation_steps)
            val_loss = validate_loop(model, dataloader, device)

            # Save checkpoints
            checkpoint_path = output_dir / f"model_epoch_{epoch + 1}.pt"
            output_dir.mkdir(parents=True, exist_ok=True)
            torch.save(model.state_dict(), checkpoint_path)
            print(f"Model saved to {checkpoint_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
