import sys
import os
import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context

# Додаємо корінь проєкту, щоб бачити 'src'
sys.path.insert(0, os.getcwd())

from src.models import Base

# Налаштування БД
DATABASE_URL = "sqlite+aiosqlite:///test.db"

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    connectable = create_async_engine(DATABASE_URL, poolclass=None)
    
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
        
    await connectable.dispose()

# Запуск асинхронної функції
if __name__ == "__main__":
    asyncio.run(run_migrations_online())