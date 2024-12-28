from datasets import load_dataset
import os

def clean_and_save_streaming(output_file):
    dataset = load_dataset("para_crawl", "enes", split="train", streaming=True)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        f.write("en,es\n")

        for i, example in enumerate(dataset):
            src, tgt = example["translation"]["en"], example["translation"]["es"]
            if (3 <= len(src.split()) <= 128 and 3 <= len(tgt.split()) <= 128 and
                "http" not in src and "www." not in src and
                "http" not in tgt and "www." not in tgt):
                f.write(f"{src},{tgt}\n")

    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    output_file = "./processed/cleaned_en_es.csv"
    clean_and_save_streaming(output_file)