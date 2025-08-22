from sqlalchemy import Column, BigInteger, String, Integer, Boolean, Double, Text, ForeignKey, DateTime, func
from app.db.db_connect import Base
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = "orders"

    id = Column("order_id", BigInteger, primary_key=True, index=True)
    address = Column(String(255))
    email = Column(String(255))
    fullname = Column(String(100))
    order_date = Column(DateTime, default=func.now())
    order_note = Column(Text)
    order_status = Column(String(50))
    phone = Column(String(50))
    total_amount = Column(Double)
    user_id = Column(BigInteger, ForeignKey("user.user_id"))

    created_by = Column(BigInteger)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)

    # Relationships
    details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")