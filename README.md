# 🤖 AI Freelance Lead Generator & Cover Letter Bot

Асинхронный инструмент для автоматического мониторинга заказов с фриланс-бирж (Habr Freelance) с нейросетевым анализом ТЗ и автогенерацией персонализированных сопроводительных писем на базе OpenAI API (GPT-4o).

## ⚡ Особенности
- 📡 **Асинхронный парсинг RSS** — моментальное обнаружение свежих публикаций заказов через `aiohttp` и `feedparser`.
- 🧠 **ИИ-Фильтрация и скоринг** — GPT-4o оценивает сложность и адекватность ТЗ по шкале от 1 до 10.
- ✍️️ **Автогенерация Cover Letter** — создание готового продающего отклика под конкретные требования заказчика.
- 🗄 **SQLite & Asyncio** — защита от повторной отправки обрабатываемых заказов через `aiosqlite`.
- 📲 **Telegram-уведомления** — аккуратно сформатированные карточки лидов с моноширинным блоком для быстрого копирования текста отклика.

## 🛠 Стек технологий
- **Python 3.10+**
- **aiogram 3.x**
- **OpenAI API (GPT-4o-mini)**
- **aiohttp / feedparser**
- **aiosqlite**

## 🚀 Быстрый запуск

1. Клонировать репозиторий:
```bash
git clone [https://github.com/fallenworked/ai-freelance-leadgen.git](https://github.com/fallenworked/ai-freelance-leadgen.git)
cd ai-freelance-leadgen
```

2. Установить зависимости:
```bash
pip install -r requirements.txt
```

3. Указать токены в `config.py` или файле `.env`:
```env
BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
OPENAI_API_KEY=sk-proj-your_openai_api_key
```

4. Запустить бота:
```bash
python main.py
```

## 👨‍💻 Автор
- **GitHub**: [fallenworked](https://github.com/fallenworked)
- **Telegram**: [@caxaold](https://t.me/caxaold)
