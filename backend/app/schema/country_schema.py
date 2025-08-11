from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class CountryCreate(BaseModel):
    country_name: str

class CountryOut(BaseModel):
    country_id: int
    country_name: str
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True