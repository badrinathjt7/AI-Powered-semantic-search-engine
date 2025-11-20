import os
from pypdf import PdfReader

def extract_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_from_txt(file):
    return file.read().decode("utf-8")

def load_files(files):
    documents = []
    for file in files:
        if file.name.endswith(".pdf"):
            text = extract_from_pdf(file)
        else:
            text = extract_from_txt(file)
        documents.append({"name": file.name, "content": text})
    return documents
