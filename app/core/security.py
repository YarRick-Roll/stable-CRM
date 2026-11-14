from datetime import datetime, timedelta, timezone
import jwt
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher

from app.config import settings

# 1. Настройка хеширования паролей через bcrypt
password_hash = PasswordHash((BcryptHasher(),))

# 2. Алгоритм цифровой подписи токена
ALGORITHM = "HS256"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Сверяет открытый пароль с хешем из базы данных."""
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Превращает сырой пароль в безопасный bcrypt-хеш."""
    return password_hash.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Создает подписанный JWT-токен с данными и сроком жизни."""
    to_encode = data.copy()

    # Рассчитываем срок годности токена
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    
    # Подписываем токен нашим секретным ключом
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
