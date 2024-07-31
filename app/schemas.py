from pydantic import BaseModel
from typing import Optional


class DeviceBase(BaseModel):
    name: str
    type: str
    login: str
    password: str
    location_id: int
    api_user_id: int


class DeviceCreate(DeviceBase):
    pass


class DeviceUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None
    location_id: Optional[int] = None
    api_user_id: Optional[int] = None


class DeviceResponse(DeviceBase):
    id: int

    class Config:
        from_attributes = True
