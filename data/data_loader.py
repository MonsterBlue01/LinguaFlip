from datasets import load_dataset
import os

def clean_and_save_streaming(output_file, chuck_size = 10000):
    dataset = load_dataset("para_crawl", "enes", split="train", streaming=True)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        f.write("en,es\n")

    cleaned_chuck = []
    for i, example in enumerate(dataset):
        src, tgt = example["translation"]["en"], example["translation"]["es"]
        if 3 <= len(src.split()) <= 128 and 3 <= len(tgt.split()) <= 128:
            cleaned_chuck.append(f"{src},{tgt}\n")

        if (i + 1) % chuck_size == 0:
            with open(output_file, "a") as f:
                f.writelines(cleaned_chuck)
            cleaned_chuck = []

    if cleaned_chuck:
        with open(output_file, "a") as f:
            f.writelines(cleaned_chuck)

    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    output_file = "./processed/cleaned_en_es.csv"
    clean_and_save_streaming(output_file)