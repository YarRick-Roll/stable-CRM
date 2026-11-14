from pydantic import BaseModel, ConfigDict

class HorseBase(BaseModel):
    name: str
    birth_year: int| None= None
    owner_name: str | None = None
    max_daily_minutes: int = 180
    is_active: bool = True

class HorseCreate(HorseBase):
    pass

class HorseUpdate(BaseModel):
    name: str | None = None
    birth_year: int| None= None
    owner_name: str | None = None
    max_daily_minutes: int | None = None
    is_active: bool | None = None

class HorseRead(HorseBase):
    id: int
    model_config = ConfigDict(from_attributes=True)