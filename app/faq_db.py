from csv import DictReader


from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import shutil, os, csv
from app.config import (
    EMBEDDING_MODEL_NAME,
    CHROMA_PERSIST_DIRECTORY,
    CHROMA_FILE,
    CHROMA_COLLECTION_NAME,
)


embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

csv_path = "./app/faq.csv"

texts = []
metadatas = []
with open(csv_path, "r", encoding="utf-8") as f:
    reader: DictReader[str] = csv.DictReader(f, delimiter="|")
    for row in reader:
        question = (row.get("question") or "").strip()
        answer = (row.get("answer") or "").strip()
        if question:
            texts.append(question)
            metadatas.append({"answer": answer})

if os.path.exists(CHROMA_PERSIST_DIRECTORY):
    if os.path.isdir(CHROMA_PERSIST_DIRECTORY):
        shutil.rmtree(CHROMA_PERSIST_DIRECTORY)

vector_store = Chroma.from_texts(
    texts=texts,
    embedding=embedding_model,
    metadatas=metadatas,
    collection_name=CHROMA_COLLECTION_NAME,
    persist_directory=CHROMA_PERSIST_DIRECTORY,
)

if os.path.exists(CHROMA_FILE):
    shutil.copy(CHROMA_FILE, "./app/faq.db")

print("✅ База знаний успешно создана: faq.db (SQLite)")
