import os
import asyncio
from aiogram import Bot, Dispatcher
import logging
from app.config import (
    BOT_TOKEN,
    CHROMA_PERSIST_DIRECTORY,
    CHROMA_FILE,
)

async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN not found in environment variables!")

    if not os.path.isdir(CHROMA_PERSIST_DIRECTORY) or not os.path.exists(CHROMA_FILE):
        print("ERROR: Chroma vector store not found (./chroma_db)!")
        print("Please run: python3 -m app.faq_db to initialize the vector store.")
        return

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    # Импортирует маршрутизатор только после проверки существования хранилища Chroma, чтобы избежать побочных эффектов при импорте.
    from app.handlers import router
    dp.include_router(router)
    print("✅ Бот запущен и готов к работе!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
