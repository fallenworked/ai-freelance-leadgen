import aiosqlite

class Database:
    def __init__(self, db_path: str = "leadgen.db"):
        self.db_path = db_path

    async def init_db(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS processed_tasks (
                    task_id TEXT PRIMARY KEY,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            await db.commit()

    async def is_task_processed(self, task_id: str) -> bool:
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT 1 FROM processed_tasks WHERE task_id = ?", (task_id,)) as cursor:
                row = await cursor.fetchone()
                return row is not None

    async def add_task(self, task_id: str):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("INSERT OR IGNORE INTO processed_tasks (task_id) VALUES (?)", (task_id,))
            await db.commit()
