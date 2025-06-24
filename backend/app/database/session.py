from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # Exemplo SQLite com async

Base = declarative_base()

# Criar a engine async
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

# Criar sessionmaker async — para abrir sessões (transações) com o banco
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Dependência para injetar a sessão no FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)