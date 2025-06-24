from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.utils.hash import get_password_hash, verify_password

async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.hashed_password),
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def update_user(db: AsyncSession, username: str, user_data: UserCreate):
    stmt = (
        update(User)
        .where(User.username == username)
        .values(
            email=user_data.email,
            hashed_password=get_password_hash(user_data.password)
        )
        .execution_options(synchronize_session="fetch")
    )
    await db.execute(stmt)
    await db.commit()
    return await get_user_by_username(db, username)

async def delete_user(db: AsyncSession, username: str):
    stmt = delete(User).where(User.username == username)
    await db.execute(stmt)
    await db.commit()
    return {"message": f"User {username} deleted"}

async def create_admin_user(db: AsyncSession):
    admin = await get_user_by_username(db, "admin")
    if not admin:
        new_admin = User(
            username="admin",
            email="admin@example.com",
            hashed_password=get_password_hash("admin")
        )
        db.add(new_admin)
        await db.commit()
        await db.refresh(new_admin)
        print("Usuário admin criado com sucesso.")
    else:
        print("Usuário admin já existe.")