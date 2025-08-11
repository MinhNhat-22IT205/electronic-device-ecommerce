from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base

class CustomerBank(Base):
    """
    Junction table linking customers to bank accounts.
    Tracks bank account details and audit information.
    """
    __tablename__ = "customer_bank"

    customer_bank_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    bank_account_number = Column(String(255), nullable=False)
    bank_id = Column(BigInteger, ForeignKey("bank.bank_id"), nullable=False)
    customer_id = Column(BigInteger, ForeignKey("customer.customer_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)