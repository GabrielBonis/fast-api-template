from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from app.api.v1 import users, auth
from app.core.config import settings
import asyncio
from app.database.session import engine, init_db, get_db, AsyncSessionLocal
from app.crud.user import create_admin_user
from app.models.user import User


app = FastAPI(
    title="Project",
    openapi_url="/openapi.json"
)

# Permitir CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas da API
app.include_router(auth.router, tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# Evento de Inicialização - Inicia banco + cria user admin
@app.on_event("startup")
async def on_startup():
    await init_db()
    async with AsyncSessionLocal() as session:
        await create_admin_user(session)


# Evento de Desligamento
@app.on_event("shutdown")
async def on_shutdown():
    await engine.dispose()
