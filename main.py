import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import settings
from bot import router, send_lead_notification
from services import HabrFreelanceParser, AIAnalyzer
from database import db

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

async def lead_monitoring_loop(bot: Bot):
    parser = HabrFreelanceParser()
    ai = AIAnalyzer()

    logging.info("🚀 Мониторинг заказов запущен...")

    while True:
        try:
            tasks = await parser.fetch_latest_tasks()
            for task in reversed(tasks):  # Обрабатываем от старых к новым
                if not await db.is_task_processed(task["id"]):
                    logging.info(f"Найдено новое задание: {task['title']}")
                    
                    # Генерация отклика через OpenAI
                    ai_data = await ai.analyze_task_and_generate_offer(
                        title=task["title"], 
                        description=task["description"]
                    )
                    
                    # Отправляем только качественные заказы (оценка 6+)
                    if ai_data.get("score", 0) >= 6:
                        await send_lead_notification(bot, task, ai_data)
                    
                    # Запоминаем задание
                    await db.add_task(task["id"])
                    
                    # Небольшая пауза между вызовами OpenAI
                    await asyncio.sleep(2)
        except Exception as e:
            logging.error(f"Ошибка в цикле мониторинга: {e}")

        await asyncio.sleep(settings.CHECK_INTERVAL_SECONDS)

async def main():
    await db.init_db()
    
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    # Фоновая таска парсинга и ИИ-анализа
    asyncio.create_task(lead_monitoring_loop(bot))

    logging.info("🤖 Запуск Telegram бота...")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
