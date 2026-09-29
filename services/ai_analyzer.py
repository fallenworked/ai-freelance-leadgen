import logging
from openai import AsyncOpenAI
from config import settings

class AIAnalyzer:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def analyze_task_and_generate_offer(self, title: str, description: str) -> dict:
        """
        Анализирует заказ, выставляет оценку адекватности (1-10) 
        и генерирует готовый персональный отклик (Cover Letter).
        """
        prompt = f"""
Ты — опытный Python-разработчик на фрилансе. Проанализируй этот заказ.

Заголовок: {title}
Описание: {description}

Ответь строго в формате JSON со следующими полями:
1. "score": оценка качества и адекватности ТЗ от 1 до 10 (целое число).
2. "tech_stack": список ключевых технологий через запятую (например: "Python, aiogram, PostgreSQL").
3. "summary": краткая суть заказа в 1 предложении.
4. "cover_letter": готовый, вежливый и продающий отклик на заказ от первого лица (не более 4-5 предложений). Покажи понимание задачи и предложи решение.

Формат вывода:
{{
    "score": 9,
    "tech_stack": "Python, Asyncio, Telegram Bot API",
    "summary": "Разработка Telegram-бота для приёма заявок с интеграцией в Google Таблицы.",
    "cover_letter": "Здравствуйте! Ознакомился с вашим заданием. Имею богатый опыт разработки асинхронных ботов на aiogram 3. Готов реализовать интеграцию с Google Таблицами через официальный API. Напишите мне в личные сообщения, чтобы обсудить детали и приступить к работе!"
}}
"""

        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                temperature=0.7
            )
            import json
            result = json.loads(response.choices[0].message.content)
            return result
        except Exception as e:
            logging.error(f"Ошибка при запросе к OpenAI API: {e}")
            return {
                "score": 5,
                "tech_stack": "Не определено",
                "summary": "Ошибка генерации ИИ",
                "cover_letter": "Не удалось сгенерировать отклик из-за ошибки API."
            }
