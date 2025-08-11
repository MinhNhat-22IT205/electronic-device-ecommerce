from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base

class Category(Base):
    """
    Represents a product category in the system.
    Tracks category details and audit information.
    """
    __tablename__ = "category"

    category_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    category_name = Column(String(255), nullable=False, index=True)
    category_image_path = Column(String(255))
    category_status = Column(String(50))
    description = Column(String(255))
    parent_id = Column(Integer)
    is_activated = Column(Boolean, default=True, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)