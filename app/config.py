import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

EMBEDDING_MODEL_NAME = "ai-forever/ru-en-RoSBERTa"
CHROMA_PERSIST_DIRECTORY = "./app/chroma_db"
CHROMA_FILE = os.path.join(CHROMA_PERSIST_DIRECTORY, "chroma.sqlite3")
CHROMA_COLLECTION_NAME = "faq"