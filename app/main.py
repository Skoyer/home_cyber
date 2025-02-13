# main.py
from fastapi import FastAPI
from .controllers.customer_controller import router as customer_router

app = FastAPI()

app.include_router(customer_router, prefix="/api", tags=["Customers"])

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD API"}