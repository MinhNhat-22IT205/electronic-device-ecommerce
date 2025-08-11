from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class CustomerCreate(BaseModel):
    customeremail: EmailStr
    customerpassword: str
    customer_phone: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    country_id: int

class CustomerOut(BaseModel):
    customer_id: int
    customeremail: EmailStr
    customer_image: Optional[str] = None
    customerpassword: str
    customer_phone: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_email_verified: bool
    registration_date: Optional[datetime] = None
    country_id: int
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True