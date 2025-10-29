import asyncio
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from app.vector_store import search_faq


router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я эхо-бот с базой знаний компании <b>First Bit</b>.\n\n"
        "Я могу:\n"
        "• Повторять ваши сообщения (эхо-ответ)\n"
        "• Отвечать на вопросы через команду /faq &lt;запрос&gt;\n\n"
        "Попробуйте отправить любое сообщение или использовать /faq",
        parse_mode="HTML",
    )


@router.message(Command("help"))
async def cmd_start(message: Message):
    await message.answer(
        "Я могу:\n"
        "• Повторять ваши сообщения (эхо-ответ)\n"
        "• Отвечать на вопросы через команду /faq &lt;запрос&gt;\n\n"
        "Попробуйте отправить любое сообщение или использовать /faq",
        parse_mode="HTML",
    )


@router.message(Command("faq"))
async def cmd_faq(message: Message):
    """Handle /faq command."""
    parts = message.text.split(maxsplit=1)
    query = parts[1].strip() if len(parts) > 1 else ""
    
    if not query:
        await message.answer(
            "Использование: /faq <запрос>\n"
            "Пример: /faq как установить зависимости"
        )
        return
    
    results = await asyncio.to_thread(search_faq, query)
    
    if not results:
        await message.answer(f"Не найдено подходящих ответов для запроса: {query}")
        return
    
    response = f"📚 Результаты поиска для: '{query}'\n\n"
    response += f"❓ {results[0][0]}\n"
    response += f"📝 {results[0][1]}"
    
    await message.answer(response)


@router.message(F.text)
async def echo_handler(message: Message):
    user_text = message.text
    await message.answer(
        f"Эхо: {user_text}"
    )
