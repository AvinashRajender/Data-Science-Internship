from classifier import classify_document
from ocr_extract import extract_text
from field_mapper import extract_fields
from classifier import classify_document
from ocr_extract import extract_text
from field_mapper import extract_fields
from confidence import score_fields

def process_document(file_path):
    text = extract_text(file_path)
    doc_type = classify_document(text)
    fields = extract_fields(doc_type, text)
    scored_fields, needs_review = score_fields(fields)

    return {
        "file": file_path,
        "document_type": doc_type,
        "fields": scored_fields,
        "needs_review": needs_review
    }

if __name__ == "__main__":
    import os, json
    results = []
    for file in os.listdir("data"):
        if file.endswith((".jpg", ".jpeg", ".png", ".pdf")):
            results.append(process_document(os.path.join("data", file)))
    with open("outputs/results.json", "w") as f:
        json.dump(results, f, indent=2)
