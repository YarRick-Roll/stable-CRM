from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

# 1. Движок подключения
engine = create_async_engine(
    settings.database_url,
    echo=True,  # Логировать SQL-запросы в консоль
)

# 2. Фабрика асинхронных сессий
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# 3. Базовый класс для всех моделей
class Base(DeclarativeBase):
    pass

# 4. Зависимость для получения сессии БД в эндпоинтах
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
