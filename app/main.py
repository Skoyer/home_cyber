# main.py
from fastapi import FastAPI
from .controllers.customer_controller import router as customer_router

from app.controllers.nmap_scan_controller import router as nmap_scan_router
from app.controllers.file_upload_controller import router as file_upload_router



app = FastAPI(title="FastAPI MVC CRUD Postgres API", version="0.1.0")

app.include_router(customer_router, prefix="/api", tags=["Customers"])
app.include_router(nmap_scan_router, prefix="/api/v1")
app.include_router(file_upload_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD API"}