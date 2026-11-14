from typing import Annotated, Sequence
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.core.security import ALGORITHM
from app.database import get_db
from app.models.user import User, UserRole
from app.schemas.user import TokenData

# 1. Говорим FastAPI, откуда извлекать токен из заголовка Authorization
# tokenUrl указывает на эндпоинт логина (нужно для интерактивной документации Swagger UI)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# 2. Функция извлечения текущего пользователя по JWT-токену
async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось подтвердить учетные данные",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Расшифровываем токен нашим секретным ключом
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        email: str | None = payload.get("sub")
        role: str | None = payload.get("role")

        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email, role=role)
    except jwt.PyJWTError:
        raise credentials_exception

    # Ищем пользователя в базе данных PostgreSQL
    result = await db.execute(select(User).where(User.email == token_data.email))
    user = result.scalar_one_or_none()

    if user is None:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь заблокирован",
        )

    return user


# 3. Фабрика проверки ролей (RBAC)
class RoleChecker:
    """Проверяет, входит ли роль текущего пользователя в список разрешенных ролей."""

    def __init__(self, allowed_roles: Sequence[UserRole]) -> None:
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: Annotated[User, Depends(get_current_user)]) -> User:
        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Недостаточно прав для выполнения этой операции",
            )
        return current_user
