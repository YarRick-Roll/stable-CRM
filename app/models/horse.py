import enum
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Horse(Base):
    __tablename__ = "horses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_year: Mapped[int|None] = mapped_column(nullable=True)
    owner_name: Mapped[str|None] = mapped_column(String(255), nullable=True)
    max_daily_minutes: Mapped[int] = mapped_column(default=180,nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
