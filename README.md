# **LinguaFlip: English-Spanish Translation System**

## **Project Overview**
LinguaFlip is a bilingual translation system designed to efficiently translate between English and Spanish. The system leverages state-of-the-art Transformer models and is optimized for mid-tier hardware (RTX 4060), balancing translation accuracy and performance.

---

## **Features**
- **Bidirectional Translation**:
  - English → Spanish
  - Spanish → English
- **Optimized Training**:
  - Supports mixed precision (FP16) for reduced memory usage.
  - Efficient Attention mechanisms (e.g., Performer, Linformer) for scalability.
- **Deployment Ready**:
  - API-based translation service using FastAPI for easy integration.

---

## **Technologies**
- **Model**: Transformer-based Encoder-Decoder architecture (e.g., MarianMT, T5-small).
- **Framework**: PyTorch and Hugging Face Transformers.
- **Preprocessing**: SentencePiece for tokenization and vocabulary management.
- **Optimization**: ONNX and TensorRT for deployment efficiency.

---

## **Data**
- **Dataset**: ParaCrawl English-Spanish parallel corpus.
- **Preprocessing**:
  - Data cleaning: Removal of noise, outliers, and non-aligned sentences.
  - Sentence length filtering: Keeping sentences with 3-128 tokens.

---

## **File Structure**
```plaintext
.
├── data
│   ├── data_loader.py         # Script for downloading and preprocessing data
│   ├── processed              # Directory for cleaned datasets
│   │   ├── cleaned_en_es.csv  # Cleaned English-Spanish dataset
│   │   └── README.md
│   └── raw                    # Directory for raw datasets
│       └── README.md
├── main.py                    # Entry point for the project
├── models
│   ├── evaluate.py            # Evaluation script for trained models
│   ├── pretrained.py          # Loading pre-trained models
│   └── train.py               # Training script
├── outputs
│   ├── checkpoints            # Model checkpoints
│   ├── logs                   # Training and evaluation logs
│   └── translations           # Sample translations
├── scripts
│   ├── deploy.py              # Deployment script for serving the model
│   └── export_model.py        # Script for exporting the model
├── utils
│   ├── data_utils.py          # Data-related utility functions
│   ├── eval_utils.py          # Evaluation-related utility functions
│   └── model_utils.py         # Model-related utility functions
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview (this file)
```

---

## **Getting Started**
### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/linguaflip.git
   cd linguaflip
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Preprocessing**
Run the `data_loader.py` script to clean and preprocess the ParaCrawl dataset:
```bash
python3 data/data_loader.py
```

---

## **Next Steps**
- **Train the Model**:
  Implement `train.py` to fine-tune a pre-trained MarianMT or T5-small model.
- **Evaluate the Model**:
  Use `evaluate.py` to calculate BLEU and SacreBLEU scores.
- **Deploy the Model**:
  Use `deploy.py` to serve translations via FastAPI.