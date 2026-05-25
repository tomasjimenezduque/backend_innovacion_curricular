import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from models.base import Base

load_dotenv()

DATABASE_URL = os.getenv("DB_POSTGRES")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL no está configurada en las variables de entorno")

# Neon usa postgresql:// pero SQLAlchemy async necesita postgresql+asyncpg://
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # ← False en producción para no llenar logs
    future=True
)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with SessionLocal() as session:
        yield session