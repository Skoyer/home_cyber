# schemas/customer_schema.py
from pydantic import BaseModel, EmailStr, IPvAnyAddress
from datetime import datetime
from typing import Optional

class CustomerSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None

    class Config:
        orm_mode = True

class NmapScanDataSchema(BaseModel):
    id: Optional[int] = None
    ip_address: IPvAnyAddress
    mac_address: str
    hostname: Optional[str]
    os: Optional[str]
    status: str
    uploaded_at: Optional[datetime]

    class Config:
        orm_mode = True
