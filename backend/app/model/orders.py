from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base

class Orders(Base):
    """
    Represents an order placed by a customer.
    Tracks order details and audit information.
    """
    __tablename__ = "orders"

    order_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    address_1 = Column(String(255))
    address_2 = Column(String(255))
    company_name = Column(String(255))
    email = Column(String(255), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    order_date = Column(DateTime, default=func.now(), nullable=False)
    order_note = Column(String(255))
    order_status = Column(String(50), nullable=False)
    phone = Column(String(20))
    total_amount = Column(Float, nullable=False, default=0.0)
    zipcode = Column(String(20))
    city_id = Column(BigInteger, ForeignKey("city.city_id"), nullable=False)
    customer_id = Column(BigInteger, ForeignKey("customer.customer_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)
