from sqlalchemy import Column, BigInteger, String, Boolean, DateTime

from backend.app.db.db_connect import Base


class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    password = Column(String(255))
    image = Column(String(255))
    is_email_verified = Column(Boolean, default=False)
    registration_date = Column(DateTime)
    created_by = Column(BigInteger)
    created_at = Column(DateTime)
    updated_by = Column(BigInteger)
    updated_at = Column(DateTime)
    deleted_by = Column(BigInteger)
    deleted_at = Column(DateTime)
