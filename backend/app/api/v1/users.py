from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.crud import user as crud_user
from app.schemas.user import UserCreate, UserOut
from app.core.security import get_current_user
from typing import List

router = APIRouter()

@router.get("/", response_model=List[UserOut])
async def list_users(
    db: AsyncSession = Depends(get_db),
    current_user: UserOut = Depends(get_current_user)
):
    return await crud_user.get_users(db)

@router.get("/{username}", response_model=UserOut)
async def get_user(
    username: str,
    db: AsyncSession = Depends(get_db),
    current_user: UserOut = Depends(get_current_user)
):
    db_user = await crud_user.get_user_by_username(db, username)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user

@router.post("/", response_model=UserOut)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
    # current_user: UserOut = Depends(get_current_user)  # opcional: pode deixar livre o cadastro
):
    return await crud_user.create_user(db, user)

@router.put("/{username}", response_model=UserOut)
async def update_user(
    username: str,
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
    current_user: UserOut = Depends(get_current_user)
):
    return await crud_user.update_user(db, username, user)

@router.delete("/{username}")
async def delete_user(
    username: str,
    db: AsyncSession = Depends(get_db),
    current_user: UserOut = Depends(get_current_user)
):
    return await crud_user.delete_user(db, username)