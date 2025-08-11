from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base

class City(Base):
    """
    Represents a city in the system.
    Tracks city details and audit information.
    """
    __tablename__ = "city"

    city_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    city_name = Column(String(255), nullable=False, index=True)
    country_id = Column(BigInteger, ForeignKey("country.country_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)