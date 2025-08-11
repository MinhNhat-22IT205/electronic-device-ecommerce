from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base

class Customer(Base):
    """
    Represents a customer in the system.
    Tracks customer details, authentication, and audit information.
    """
    __tablename__ = "customer"

    customer_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    customeremail = Column(String(255), unique=True, nullable=False, index=True)
    customer_image = Column(String(255))
    customerpassword = Column(String(255), nullable=False)
    customer_phone = Column(String(20))
    first_name = Column(String(100))
    last_name = Column(String(100))
    is_email_verified = Column(Boolean, default=False, nullable=False)
    registration_date = Column(DateTime, default=func.now(), nullable=False)
    country_id = Column(BigInteger, ForeignKey("country.country_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)