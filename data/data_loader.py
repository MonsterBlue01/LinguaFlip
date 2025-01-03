import pandas as pd
from transformers import MarianTokenizer
import torch
import os
import gc

tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")

def process_chunk(chunk, tokenizer, max_length=128):
    try:
        # Remove missing values ​​and create a copy to avoid SettingWithCopyWarning
        chunk = chunk.dropna(subset=["en", "es"]).copy()

        # Use .loc for assignment to avoid warnings
        chunk.loc[:, "en"] = chunk["en"].astype(str)
        chunk.loc[:, "es"] = chunk["es"].astype(str)

        # Filter invalid rows using vectorized operations
        valid_chunk = chunk[
            (chunk["en"].str.len() >= 3) & (chunk["en"].str.len() <= 128) &
            (chunk["es"].str.len() >= 3) & (chunk["es"].str.len() <= 128) &
            (~chunk["en"].str.contains("http|www.", regex=True)) &
            (~chunk["es"].str.contains("http|www.", regex=True))
        ]

        print(f"Valid rows in chunk: {len(valid_chunk)}")  # For debugging

        if valid_chunk.empty:
            print("No valid rows in this chunk.")
            return None

        # Encoding using batch processing
        src_encodings = tokenizer(
            valid_chunk["en"].tolist(),
            max_length=max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )
        tgt_encodings = tokenizer(
            valid_chunk["es"].tolist(),
            max_length=max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )

        print(f"Tokenized chunk: src shape {src_encodings['input_ids'].shape}, tgt shape {tgt_encodings['input_ids'].shape}")  # 调试信息

        return {"src": src_encodings["input_ids"], "tgt": tgt_encodings["input_ids"]}
    except Exception as e:
        print(f"Error in process_chunk: {e}")
        return None

def save_combined_chunks(chunk_list, output_dir, file_idx):
    """Save a combined list of chunks to a single .pt file."""
    print(f"Saving combined_chunks of length {len(chunk_list)}...")
    for i, chunk in enumerate(chunk_list):
        print(f"  Chunk {i}: src shape {chunk['src'].shape}, tgt shape {chunk['tgt'].shape}")

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"combined_chunk_{file_idx}.pt")

    # Combine src and tgt encodings from all chunks
    combined_data = {"src": [], "tgt": []}
    for chunk_data in chunk_list:
        combined_data["src"].append(chunk_data["src"])
        combined_data["tgt"].append(chunk_data["tgt"])

    # Concatenate tensors along the batch dimension
    combined_data["src"] = torch.cat(combined_data["src"], dim=0)
    combined_data["tgt"] = torch.cat(combined_data["tgt"], dim=0)

    torch.save(combined_data, output_file)
    print(f"Saved combined chunk {file_idx} to {output_file}")

def merge_intermediate_files(intermediate_files, output_dir):
    """Merge multiple intermediate files into one or more larger files."""
    merged_data = []  # Change to list
    final_file_idx = 0

    for file_idx, intermediate_file in enumerate(intermediate_files):
        print(f"Merging {intermediate_file}...")
        data = torch.load(intermediate_file)
        merged_data.append(data)

        if len(merged_data) >= 20:  # Merge 20 intermediate files each time
            save_combined_chunks(merged_data, output_dir, final_file_idx)
            print(f"Merged file {final_file_idx} saved.")
            merged_data = []  # Reset List
            final_file_idx += 1

            # Manually freeing memory
            gc.collect()

    # Save remaining data
    if merged_data:
        save_combined_chunks(merged_data, output_dir, final_file_idx)
        print(f"Final merged file {final_file_idx} saved.")
        gc.collect()

def process_large_dataset(input_file, output_dir, tokenizer, chunk_size=25000, intermediate_size=10):
    chunk_idx = 0
    intermediate_file_idx = 0
    combined_chunks = []  # Change to list
    intermediate_files = []

    try:
        for chunk in pd.read_csv(input_file, chunksize=chunk_size, delimiter=",", on_bad_lines="skip"):
            chunk_idx += 1
            print(f"Processing chunk {chunk_idx}...")

            processed_data = process_chunk(chunk, tokenizer)
            if processed_data:
                combined_chunks.append(processed_data)  # Add to List
                print(f"Chunk {chunk_idx} processed and added to combined_chunks.")
            else:
                print(f"Chunk {chunk_idx} has no valid data and was skipped.")

            # Save as intermediate file
            if chunk_idx % intermediate_size == 0:
                intermediate_file = os.path.join(output_dir, f"intermediate_{intermediate_file_idx}.pt")
                save_combined_chunks(combined_chunks, output_dir, intermediate_file_idx)
                intermediate_files.append(intermediate_file)
                print(f"Intermediate file {intermediate_file_idx} saved.")
                combined_chunks = []  # Reset List
                intermediate_file_idx += 1

        # Save the remaining data as the final intermediate file
        if combined_chunks:
            intermediate_file = os.path.join(output_dir, f"intermediate_{intermediate_file_idx}.pt")
            save_combined_chunks(combined_chunks, output_dir, intermediate_file_idx)
            intermediate_files.append(intermediate_file)
            print(f"Final intermediate file {intermediate_file_idx} saved.")
            combined_chunks = []  # Reset List

        # Merge intermediate files into larger files
        if intermediate_files:
            merge_intermediate_files(intermediate_files, output_dir)

    except Exception as e:
        print(f"Critical error while processing dataset: {e}")

if __name__ == "__main__":
    input_file = "./processed/cleaned_en_es.csv"
    output_dir = "./processed/tokenized"

    process_large_dataset(input_file, output_dir, tokenizer, chunk_size=25000, intermediate_size=10)
    print("Tokenization complete")
