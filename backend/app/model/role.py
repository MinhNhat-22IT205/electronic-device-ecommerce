from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base
class Role(Base):
    """
    Represents a role in the system, used for both admins and customers.
    Tracks role details and audit information.
    """
    __tablename__ = "role"

    role_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    role_name = Column(String(255), nullable=False, index=True)
    description = Column(String(255))
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)