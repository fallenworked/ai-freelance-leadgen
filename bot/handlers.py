from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "🤖 **AI Freelance Lead Generator Bot запущен!**\n\n"
        "Бот отслеживает новые заказы на фрилансе, анализирует их с помощью GPT-4o "
        "и присылает готовые продающие отклики в этот чат."
    )
