import torch
from torch.utils.data import DataLoader, Dataset
from transformers import MarianMTModel, MarianTokenizer, AdamW
from transformers import get_scheduler
from tqdm import tqdm
from pathlib import Path
import os

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
            data = torch.load(file, map_location='cpu')  # Use CPU loading to reduce GPU memory usage
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
        # Find the file where idx is located
        file_idx = 0
        while file_idx < len(self.cumulative_lengths) and idx >= self.cumulative_lengths[file_idx]:
            file_idx += 1
        
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

def train_loop(model, dataloader, optimizer, scheduler, device):
    model.train()
    total_loss = 0

    for batch in tqdm(dataloader, desc="Training"):
        src, tgt = batch
        src, tgt = src.to(device), tgt.to(device)

        # Forward pass
        outputs = model(input_ids=src, labels=tgt)
        loss = outputs.loss
        total_loss += loss.item()

        # Backward pass and optimization step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        scheduler.step()

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

            outputs = model(input_ids=src, labels=tgt)
            loss = outputs.loss
            total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    print(f"Validation Loss: {avg_loss}")
    return avg_loss

if __name__ == "__main__":
    from pathlib import Path

    # Get the absolute path of the current script
    script_path = Path(__file__).resolve()
    script_dir = script_path.parent

    # The absolute path to the build data directory
    data_dir = (script_dir / "../data/processed/tokenized").resolve()
    output_dir = (script_dir / "../outputs/checkpoints").resolve()

    # Print debug information
    print(f"Data directory path: {data_dir}")
    print(f"Output directory path: {output_dir}")

    # Hyperparameters
    num_epochs = 3
    batch_size = 8
    learning_rate = 5e-5
    model_name = "Helsinki-NLP/opus-mt-en-es"

    # Device setup
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"The equipment used is: {device}")

    # Load model and tokenizer
    print("Loading the model and tokenizer...")
    model = MarianMTModel.from_pretrained(model_name).to(device)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Prepare dataset and dataloader
    print("Preparing dataset and data loader...")
    dataset = TranslationDataset(data_dir)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=4)

    # Optimizer and scheduler
    optimizer = AdamW(model.parameters(), lr=learning_rate)
    num_training_steps = len(dataloader) * num_epochs
    scheduler = get_scheduler(
        "linear",
        optimizer=optimizer,
        num_warmup_steps=0,
        num_training_steps=num_training_steps
    )

    # Training loop
    for epoch in range(num_epochs):
        print(f"\nEpoch {epoch + 1}/{num_epochs}")
        train_loss = train_loop(model, dataloader, optimizer, scheduler, device)
        val_loss = validate_loop(model, dataloader, device)

        # Save checkpoint
        checkpoint_path = output_dir / f"model_epoch_{epoch + 1}.pt"
        output_dir.mkdir(parents=True, exist_ok=True)
        torch.save(model.state_dict(), checkpoint_path)
        print(f"Model saved to {checkpoint_path}")
