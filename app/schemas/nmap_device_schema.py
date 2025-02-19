from pydantic import BaseModel, IPvAnyAddress
from typing import Optional
from datetime import datetime

class NmapDeviceBase(BaseModel):
    ip_address: IPvAnyAddress
    mac_address: str
    hostname: Optional[str] = None
    os: Optional[str] = None
    status: str

class NmapDeviceCreate(NmapDeviceBase):
    pass

class NmapDevice(NmapDeviceBase):
    id: int
    uploaded_at: datetime

    class Config:
        from_attributes = True