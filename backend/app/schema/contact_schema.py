from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class ContactCreate(BaseModel):
    email: EmailStr
    message: str
    name: Optional[str] = None
    subject: Optional[str] = None
    customer_id: int

class ContactOut(BaseModel):
    contact_id: int
    email: EmailStr
    message: str
    name: Optional[str] = None
    subject: Optional[str] = None
    customer_id: int
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True