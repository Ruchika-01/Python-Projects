import pdfplumber

def load_pdf(path: str) -> str:
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()
import re

def normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text
