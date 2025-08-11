from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base

class ProductImage(Base):
    """
    Represents images associated with a product.
    Tracks image details and audit information.
    """
    __tablename__ = "product_image"

    product_image_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    product_image_path = Column(String(255), nullable=False)
    sort_order = Column(Integer, default=0)
    product_id = Column(BigInteger, ForeignKey("product.product_id"), nullable=False)
    color_id = Column(BigInteger, ForeignKey("color.color_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)
