# main.py
from fastapi import FastAPI
from .controllers.customer_controller import router as customer_router

app = FastAPI(title="FastAPI MVC CRUD Postgres API", version="0.1.0")

app.include_router(customer_router, prefix="/api", tags=["Customers"])


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD API"}