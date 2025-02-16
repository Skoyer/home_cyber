from sqlalchemy import Column, String, DateTime, Text, Integer
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.sql import func
from app.db.base import Base

class NmapScanData(Base):
    __tablename__ = "nmap_scan_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(INET, nullable=False)
    mac_address = Column(String(17), nullable=False)
    hostname = Column(String(255))
    os = Column(Text)
    status = Column(String(10), nullable=False)
    uploaded_at = Column(DateTime, default=func.now(), nullable=False)
