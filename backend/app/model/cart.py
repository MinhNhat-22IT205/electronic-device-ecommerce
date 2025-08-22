from sqlalchemy import Column, BigInteger, String, Integer, Boolean, Double, Text, ForeignKey, DateTime, func
from app.db.db_connect import Base
from sqlalchemy.orm import relationship

class Cart(Base):
    __tablename__ = "cart"

    id = Column("cart_id", BigInteger, primary_key=True, index=True)
    total_amount = Column(Double, default=0)
    total_item = Column(Integer, default=0)
    user_id = Column(BigInteger, ForeignKey("user.user_id"))

    created_by = Column(BigInteger)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)

    # Relationships
    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")