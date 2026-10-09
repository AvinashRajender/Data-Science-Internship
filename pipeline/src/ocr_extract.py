import easyocr
from pdf2image import convert_from_path
import os

reader = easyocr.Reader(['en'])

def extract_text(file_path):
    if file_path.lower().endswith(".pdf"):
        # Convert first page of PDF to image
        pages = convert_from_path(file_path, dpi=200)
        text = ""
        for page in pages:
            result = reader.readtext(page)
            text += " ".join([res[1] for res in result]) + "\n"
        return text
    else:
        results = reader.readtext(file_path)
        return " ".join([res[1] for res in results])
