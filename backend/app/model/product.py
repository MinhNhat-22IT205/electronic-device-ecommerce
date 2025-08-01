from sqlalchemy import Column, BigInteger, String, Integer, Boolean, Double, Text, ForeignKey, DateTime
from app.config.db_connect import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "product"

    id = Column("product_id", BigInteger, primary_key=True)
    name = Column("product_name", String(255))
    sku = Column("product_sku", String(100))
    description = Column(Text)
    camera = Column(String(100))
    cpu = Column(String(100))
    ram = Column(Integer)
    rom = Column(Integer)
    pin = Column(Integer)
    cost_price = Column(Double)
    sale_price = Column(Double)
    quantity = Column("current_quantity",Integer)
    weight = Column(Double)
    width = Column(Double)
    height = Column(Double)
    thick = Column(Double)
    is_activated = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    images = relationship("ProductImage", back_populates="product")

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

class Color(Base):
    __tablename__ = "color"

    id = Column("color_id", BigInteger, primary_key=True)
    name = Column("color_name", String(100))

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    images = relationship("ProductImage", back_populates="color")
