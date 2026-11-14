from pydantic import BaseModel, ConfigDict
from datetime import datetime

class BookingBase(BaseModel):
    horse_id: int
    service_id: int
    client_name: str
    start_time: datetime
    duration_minutes: int | None = None
    notes: str | None = None

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BaseModel):
    horse_id: int | None = None
    service_id: int | None = None
    client_name: str | None = None
    start_time: datetime | None = None
    duration_minutes: int | None = None
    status: str | None = None
    notes: str | None = None

class BookingRead(BookingBase):
    id: int
    user_id: int | None = None
    status: str
    duration_minutes: int
    model_config = ConfigDict(from_attributes=True)