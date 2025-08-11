from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from backend.app.db.db_connect import Base

class CartItem(Base):
    """
    Represents an item in a shopping cart.
    Tracks item details and audit information.
    """
    __tablename__ = "cart_item"

    cart_item_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    cart_item_sku = Column(String(255), nullable=False)
    product_price = Column(Float, nullable=False, default=0.0)
    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(Float, nullable=False, default=0.0)
    cart_id = Column(BigInteger, ForeignKey("cart.cart_id"), nullable=False)
    product_id = Column(BigInteger, ForeignKey("product.product_id"), nullable=False)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)