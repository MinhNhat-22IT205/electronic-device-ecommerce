from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base

class ProductCategory(Base):
    """
    Junction table linking products to categories.
    Tracks category assignments and audit information.
    """
    __tablename__ = "product_category"

    product_category_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    product_id = Column(BigInteger, ForeignKey("product.product_id"), nullable=False)
    category_id = Column(BigInteger, ForeignKey("category.category_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)
