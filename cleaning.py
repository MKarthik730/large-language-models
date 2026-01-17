
import re

import pdfplumber

def get_data(book_path):
    text = ""
    with pdfplumber.open(book_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def clean_book_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"^\s+|\s+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^[A-Z\s]{4,}$", "", text, flags=re.MULTILINE)
    text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\[\d+\]", "", text)
    text = re.sub(r"^-{3,}$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^.*\|.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()

def clean(name:str):
    txt=get_data(name)
    cleaned=clean_book_text(txt)
    return cleaned