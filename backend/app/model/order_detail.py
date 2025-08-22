from sqlalchemy import Column, BigInteger, String, Integer, Boolean, Double, Text, ForeignKey, DateTime, func
from app.db.db_connect import Base
from sqlalchemy.orm import relationship

class OrderDetail(Base):
    __tablename__ = "order_detail"

    id = Column("order_detail_id", BigInteger, primary_key=True, index=True)
    product_price = Column(Double)
    quantity = Column(Integer)
    total_amount = Column(Double)

    order_id = Column(BigInteger, ForeignKey("orders.order_id"))
    product_id = Column(BigInteger, ForeignKey("product.product_id"))

    created_by = Column(BigInteger)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)

    # Relationships
    order = relationship("Order", back_populates="details")
    product = relationship("Product")