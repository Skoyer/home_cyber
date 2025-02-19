from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.nmap_scan_data import NmapScanData
from app.schemas.nmap_device_schema import NmapDeviceCreate, NmapDevice
from typing import List
import pandas as pd

router = APIRouter(prefix="/nmap/devices", tags=["Nmap Devices"])

@router.post("/", response_model=List[NmapDevice])
def create_nmap_devices(devices: List[NmapDeviceCreate], db: Session = Depends(get_db)):
    """Add multiple devices from an nmap scan to the database."""
    db_devices = [
        NmapScanData(
            ip_address=str(device.ip_address),  # Convert IPv4Address to string
            mac_address=device.mac_address,
            hostname=device.hostname,
            os=device.os,
            status=device.status
        )
        for device in devices
    ]
    db.add_all(db_devices)
    db.commit()
    return db_devices

@router.get("/", response_model=List[NmapDevice])
def get_all_nmap_devices(db: Session = Depends(get_db)):
    """Retrieve all scanned nmap devices."""
    return db.query(NmapScanData).all()

@router.get("/{device_id}", response_model=NmapDevice)
def get_nmap_device(device_id: int, db: Session = Depends(get_db)):
    """Retrieve a single scanned nmap device by ID."""
    device = db.query(NmapScanData).filter(NmapScanData.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@router.delete("/{device_id}", response_model=dict)
def delete_nmap_device(device_id: int, db: Session = Depends(get_db)):
    """Delete a single scanned nmap device by ID."""
    device = db.query(NmapScanData).filter(NmapScanData.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    db.delete(device)
    db.commit()
    return {"message": "Device deleted successfully"}

# Function to load hosts_df into the database

def load_dataframe_to_db(hosts_df: pd.DataFrame, db: Session):
    """Load an entire DataFrame (hosts_df) into the database."""
    devices = [
        NmapScanData(
            ip_address=str(row["ip_address"]),  # Convert IPv4Address to string
            mac_address=row["mac_address"],
            hostname=row["hostname"],
            os=row["os"],
            status=row["status"]
        )
        for _, row in hosts_df.iterrows()
    ]
    db.add_all(devices)
    db.commit()
    return {"message": "DataFrame successfully loaded into the database."}
