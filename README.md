# ANUVAAD AI 🌐
### Breaking Language Barriers with Artificial Intelligence

**ANUVAAD AI** is an AI-powered English-to-Marathi translation application built using a fine-tuned NLLB-200 Transformer model. It helps users translate English text and dialogue into Marathi through a simple and interactive interface.

## 🚀 Features

- **English-to-Marathi Translation:** Translate English text into Marathi.
- **Dialogue Translation:** Translate longer conversations and dialogue.
- **Fine-Tuned Transformer:** Uses a fine-tuned NLLB-200 model.
- **Text Processing:** Handles long text through chunk-based processing.
- **Translation History:** View previous translations during the session.
- **Download Translation:** Download translated text.
- **Interactive UI:** Built with Streamlit.

## 🧠 Model Information

- **Base Model:** `facebook/nllb-200-distilled-600M`
- **Architecture:** Transformer (Sequence-to-Sequence)
- **Tokenizer:** NLLB AutoTokenizer
- **Source Language:** English (`eng_Latn`)
- **Target Language:** Marathi (`mar_Deva`)
- **Fine-Tuning Dataset:** AI4Bharat Samanantar (English-Marathi samples)

The model was fine-tuned for English-to-Marathi translation.

## 🛠️ Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- NLLB-200
- SentencePiece
- Streamlit

## 📂 Project Structure

```text
ANUVAAD-AI/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── src/
│   └── translator.py
│
└── models/
    └── nllb_en_mr_finetuned/
        ├── config.json
        ├── generation_config.json
        ├── model.safetensors
        ├── tokenizer.json
        └── tokenizer_config.json
```

> **Note:** The trained model files are not included in this GitHub repository because of their large size. Place your downloaded fine-tuned model inside `models/nllb_en_mr_finetuned/` before running the application.

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/gaikwadsumitsudhakar-cpu/ANUVAAD-AI.git
cd ANUVAAD-AI
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the environment**

Windows:

```bash
venv\Scripts\activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Add the fine-tuned model**

Place the downloaded model folder at:

```text
models/nllb_en_mr_finetuned/
```

**6. Run the application**

```bash
streamlit run app.py
```

## 🎯 Project Objective

The main objective of ANUVAAD AI is to make English-to-Marathi translation more accessible using modern Natural Language Processing and Transformer-based deep learning techniques.

## 👨‍💻 Developer

**Sumit Gaikwad**

AI/ML Enthusiast | Python | Deep Learning | NLP | Generative AI

---

⭐ If you find this project interesting, consider giving it a star!
