import os
import pandas as pd
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.nmap_scan_data import NmapScanData
from sqlalchemy.sql import exists
from datetime import datetime

router = APIRouter()

DATA_DIRECTORY = "app/data/"  # Define the directory for your CSV files


@router.post("/upload-new-files/")
def upload_new_files(db: Session = Depends(get_db)):
    """
    Check the data directory for new files and upload them to the database.
    """
    try:
        # List all CSV files in the directory
        files = [f for f in os.listdir(DATA_DIRECTORY) if f.endswith(".csv")]

        for file in files:
            # Check if the file has already been processed (e.g., by filename)
            file_path = os.path.join(DATA_DIRECTORY, file)
            if not db.query(NmapScanData).filter(NmapScanData.ip_address == file).first():  # Example logic for uniqueness

                # Read the CSV into a DataFrame
                df = pd.read_csv(file_path, encoding="utf-8")

                # Replace NaN with None for specific columns
                df['hostname'] = df['hostname'].fillna(value=None)  # Handle missing hostnames
                df['os'] = df['os'].fillna(value=None)  # Handle missing OS information

                # Ensure MAC addresses are strings (should already be, but ensuring)
                df['mac_address'] = df['mac_address'].astype(str)

                # Iterate over the DataFrame and add each row to the database
                for _, row in df.iterrows():
                    nmap_data = NmapScanData(
                        ip_address=row["ip_address"],
                        mac_address=row["mac_address"],
                        hostname=row.get("hostname"),
                        os=row.get("os"),
                        status=row["status"],
                        uploaded_at=datetime.utcnow(),
                    )
                    db.add(nmap_data)

                # Commit the data for this file
                db.commit()

                # Optional: Mark the file as processed by adding a record or renaming/moving the file
                print(f"Uploaded data from file: {file}")

        return {"message": "All new files have been uploaded successfully"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error processing files: {e}")
