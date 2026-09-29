import aiohttp
import feedparser
import logging
from typing import List, Dict, Any

class HabrFreelanceParser:
    # RSS-лента категории "Программирование" и "Скрипты/Боты"
    RSS_URL = "https://freelance.habr.com/tasks.rss?categories=dev_all,dev_bots,dev_scripts"

    async def fetch_latest_tasks() -> List[Dict[str, Any]]:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.RSS_URL, timeout=aiohttp.ClientTimeout(total=10)) as response:
                    if response.status == 200:
                        content = await response.text()
                        feed = feedparser.parse(content)
                        
                        tasks = []
                        for entry in feed.entries:
                            tasks.append({
                                "id": entry.id,
                                "title": entry.title,
                                "link": entry.link,
                                "description": entry.summary,
                                "published": entry.published
                            })
                        return tasks
                    logging.error(f"Ошибка получения RSS Habr Freelance: HTTP {response.status}")
            except Exception as e:
                logging.error(f"Ошибка во время парсинга RSS: {e}")
        return []
