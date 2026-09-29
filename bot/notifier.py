import logging
from aiogram import Bot
from config import settings

async def send_lead_notification(bot: Bot, task: dict, ai_data: dict):
    """Отправляет отфильтрованный заказ с разбором от ИИ в Telegram"""
    
    score_emoji = "🔥" if ai_data.get("score", 0) >= 8 else "⚡"
    
    msg = (
        f"{score_emoji} **НОВЫЙ ЛИД | Оценка ИИ: {ai_data.get('score')}/10**\n\n"
        f"📌 **Заголовок:** [{task['title']}]({task['link']})\n"
        f"🛠 **Стек:** `{ai_data.get('tech_stack')}`\n"
        f"📝 **Суть:** {ai_data.get('summary')}\n\n"
        f"💬 **Готовое сопроводительное письмо:**\n"
        f"```text\n{ai_data.get('cover_letter')}\n```"
    )

    try:
        await bot.send_message(
            chat_id=settings.TELEGRAM_CHAT_ID,
            text=msg,
            parse_mode="Markdown",
            disable_web_page_preview=False
        )
    except Exception as e:
        logging.error(f"Ошибка отправки сообщения в Telegram: {e}")
