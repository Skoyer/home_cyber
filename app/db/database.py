from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base  # Use the imported Base


load_dotenv()
# Construct the DATABASE_URL using environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

if not all([db_user, db_password, db_host, db_port, db_name]):
    raise ValueError("One or more database environment variables are missing.")

DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

print(f"Database URL: {DATABASE_URL}")  # Only for debugging; remove in production

# Create the engine for the PostgreSQL database
engine = create_engine(DATABASE_URL)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables in the database
Base.metadata.create_all(bind=engine)
