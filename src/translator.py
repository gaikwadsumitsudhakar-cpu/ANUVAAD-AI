
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class NLLBTranslator:

    def __init__(self, model_path):

        self.device = "cpu"

        print("Loading fine-tuned NLLB model...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            local_files_only=True
        )

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            model_path,
            local_files_only=True,
            low_cpu_mem_usage=True
        )

        self.model.to(self.device)
        self.model.eval()

        self.tokenizer.src_lang = "eng_Latn"

        self.target_lang = "mar_Deva"

        print("Fine-tuned model loaded successfully!")

    def translate(self, text):

        if not text.strip():
            return ""

        self.tokenizer.src_lang = "eng_Latn"

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=128
        )

        target_id = self.tokenizer.convert_tokens_to_ids(
            self.target_lang
        )

        with torch.inference_mode():

            outputs = self.model.generate(
                **inputs,
                forced_bos_token_id=target_id,
                max_new_tokens=128,
                num_beams=2
            )

        translated_text = self.tokenizer.batch_decode(
            outputs,
            skip_special_tokens=True
        )[0]

        return translated_text
