from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.config.database import Base

class Product(Base):
    """
    Represents a product in the system.
    Tracks product details, specifications, and audit information.
    """
    __tablename__ = "product"

    product_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    product_name = Column(String(255), nullable=False, index=True)
    product_sku = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text)
    camera = Column(String(255))
    cpu = Column(String(255))
    ram = Column(Integer)
    rom = Column(Integer)
    stock = Column(Integer, nullable=False)
    pin = Column(Integer)
    cost_price = Column(Float, nullable=False, default=0.0)
    sale_price = Column(Float, nullable=False, default=0.0)
    current_quantity = Column(Integer, nullable=False, default=0)
    weight = Column(Float)
    width = Column(Float)
    height = Column(Float)
    thick = Column(Float)
    is_activated = Column(Boolean, default=True, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)