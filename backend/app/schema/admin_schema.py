from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class AdminCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str
class AdminOut(BaseModel):
    admin_id: int
    email: EmailStr
    first_name: str
    last_name: str
    image: Optional[str]
    is_email_verified: bool
    registration_date: Optional[datetime]

    class Config:
        from_attributes = True