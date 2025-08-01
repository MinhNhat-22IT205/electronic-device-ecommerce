from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from app.config.db_connect import Base

class User(Base):
    __tablename__ = "user"

    id = Column("user_id", BigInteger, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(String(15))
    image = Column(String(255))
    role = Column(String(50), default="customer") 
    is_verified = Column(Boolean, default=True)
    registered_at = Column(DateTime)
