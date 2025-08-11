from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base


class Country(Base):
    """
    Represents a country in the system.
    Tracks country details and audit information.
    """
    __tablename__ = "country"

    country_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    country_name = Column(String(255), nullable=False, index=True)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)
