import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import CHAR
# from db.database import Base
from app.db.base import Base  # Import Base here


class Customer(Base):
    __tablename__ = "customers"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    address = Column(String(255), nullable=True)