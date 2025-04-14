# app/db/session.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create the async engine
# connect_args only needed for SQLite, remove for PostgreSQL
# engine = create_async_engine(settings.DATABASE_URL, pool_pre_ping=True, connect_args={"check_same_thread": False}) # For SQLite
engine = create_async_engine(settings.DATABASE_URL, pool_pre_ping=True, echo=True) # echo=True for debugging SQL

# Create a session factory bound to the engine
# expire_on_commit=False prevents attributes from being expired after commit in async context
AsyncSessionFactory = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency to get DB session
async def get_db() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session