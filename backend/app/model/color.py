from sqlalchemy import Column, BigInteger, String, Integer, Boolean, Double, Text, ForeignKey, DateTime
from app.db.db_connect import Base
from sqlalchemy.orm import relationship

class Color(Base):
    __tablename__ = "color"

    id = Column("color_id", BigInteger, primary_key=True)
    name = Column("color_name", String(100))

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    images = relationship("ProductImage", back_populates="color")
