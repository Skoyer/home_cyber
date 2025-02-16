from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.nmap_scan_data import NmapScanData
from datetime import datetime
from typing import List

router = APIRouter()

@router.post("/upload-nmap-data/")
def upload_nmap_data(data: List[dict], db: Session = Depends(get_db)):
    """
    Upload Nmap scan data into the database.
    :param data: A list of dictionaries containing scan data.
    """
    try:
        for record in data:
            nmap_data = NmapScanData(
                ip_address=record["ip_address"],
                mac_address=record["mac_address"],
                hostname=record.get("hostname"),
                os=record.get("os"),
                status=record["status"],
                uploaded_at=datetime.utcnow(),
            )
            db.add(nmap_data)
        db.commit()
        return {"message": "Data uploaded successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
