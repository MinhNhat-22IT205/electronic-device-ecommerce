from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base


class CustomerRole(Base):
    """
    Junction table linking customers to roles.
    Tracks role assignments and audit information.
    """
    __tablename__ = "customer_role"

    customer_role_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(BigInteger, ForeignKey("customer.customer_id"), nullable=False)
    role_id = Column(BigInteger, ForeignKey("role.role_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)