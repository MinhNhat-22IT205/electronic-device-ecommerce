from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base

class Contact(Base):
    """
    Represents a contact message from a customer.
    Tracks message details and audit information.
    """
    __tablename__ = "contact"

    contact_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), nullable=False)
    message = Column(String(255), nullable=False)
    name = Column(String(255))
    subject = Column(String(255))
    customer_id = Column(BigInteger, ForeignKey("customer.customer_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)
