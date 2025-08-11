from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base
class ProductReview(Base):
    """
    Represents a customer review for a product.
    Tracks review details and audit information.
    """
    __tablename__ = "product_review"

    product_review_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    comment = Column(String(255))
    rating = Column(Integer, nullable=False)
    num_comment = Column(Integer, default=0)
    customer_id = Column(BigInteger, ForeignKey("customer.customer_id"), nullable=False)
    product_id = Column(BigInteger, ForeignKey("product.product_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)