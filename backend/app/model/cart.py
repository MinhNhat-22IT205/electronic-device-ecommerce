from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base

class Cart(Base):
    """
    Represents a shopping cart in the system.
    Tracks cart details and audit information.
    """
    __tablename__ = "cart"

    cart_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    total_amount = Column(Float, nullable=False, default=0.0)
    total_item = Column(Integer, nullable=False, default=0)
    customer_id = Column(BigInteger, ForeignKey("customer.customer_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)