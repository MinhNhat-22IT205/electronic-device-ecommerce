from sqlalchemy import Column, BigInteger, String, Integer, Boolean, Double, Text, ForeignKey, DateTime
from app.db.db_connect import Base
from sqlalchemy.orm import relationship

class ProductImage(Base):
    __tablename__ = "product_image"

    id = Column("product_image_id", BigInteger, primary_key=True)
    path = Column("product_image_path", String(255))
    sort_order = Column(Integer)

    product_id = Column(BigInteger, ForeignKey("product.product_id"))
    color_id = Column(BigInteger, ForeignKey("color.color_id"))

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    product = relationship("Product", back_populates="images")
    color = relationship("Color", back_populates="images")