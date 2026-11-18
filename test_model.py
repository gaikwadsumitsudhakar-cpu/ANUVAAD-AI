
from src.translator import NLLBTranslator

MODEL_PATH = "./models/nllb_en_mr_finetuned"

translator = NLLBTranslator(MODEL_PATH)

text = """
Artificial Intelligence is transforming
the world. Machine learning helps computers
learn from data and make predictions.
"""

result = translator.translate(text)

print("\nOriginal English:")
print(text)

print("\nTranslated Marathi:")
print(result)
