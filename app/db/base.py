from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.models.nmap_scan_data import NmapScanData  # Add this import

# Ensure all models are imported here so Alembic can detect them for migrations
