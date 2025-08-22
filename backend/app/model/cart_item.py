from sqlalchemy import Column, BigInteger, String, Integer, Boolean, Double, Text, ForeignKey, DateTime, func
from app.db.db_connect import Base
from sqlalchemy.orm import relationship

class CartItem(Base):
    __tablename__ = "cart_item"

    id = Column("cart_item_id", BigInteger, primary_key=True, index=True)
    product_price = Column(Double)
    quantity = Column(Integer)
    total_price = Column(Double)

    cart_id = Column(BigInteger, ForeignKey("cart.cart_id"))
    product_id = Column(BigInteger, ForeignKey("product.product_id"))

    created_by = Column(BigInteger)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)

    # Relationships
    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")