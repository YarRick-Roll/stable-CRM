from pydantic import BaseModel, ConfigDict

class ServiceBase(BaseModel):
    name: str 
    description: str | None = None
    duration_minutes: int=60
    price: float
    is_active: bool = True

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    duration_minutes: int | None = None
    price: float | None = None
    is_active: bool | None = None

class ServiceRead(ServiceBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

