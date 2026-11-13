from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    horse_id: Mapped[int] = mapped_column(ForeignKey("horses.id"), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"), nullable=False)
    user_id: Mapped[int|None] = mapped_column(ForeignKey("users.id"), nullable=True)
    client_name: Mapped[str] = mapped_column(String(100), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False)
    duration_minutes: Mapped[int] = mapped_column(default=60,nullable=False)
    status: Mapped[str] = mapped_column(String(100),nullable=False)
    notes: Mapped[str|None] = mapped_column(Text)