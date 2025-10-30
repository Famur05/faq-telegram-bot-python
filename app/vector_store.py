from langchain_core.documents.base import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from app.config import (
    EMBEDDING_MODEL_NAME,
    CHROMA_PERSIST_DIRECTORY,
    CHROMA_COLLECTION_NAME,
)

embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

vector_store = Chroma(
    embedding_function=embedding_model,
    collection_name=CHROMA_COLLECTION_NAME,
    persist_directory=CHROMA_PERSIST_DIRECTORY,
)


def search_faq(query: str) -> list[tuple[str, str]]:
    results: list[Document] = vector_store.similarity_search(query, k=1)
    formatted: list[tuple[str, str]] = []
    for doc in results:
        question = doc.page_content
        answer = doc.metadata.get("answer", "") if doc.metadata else ""
        formatted.append((question, answer))
    return formatted
