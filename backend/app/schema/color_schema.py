from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class ColorCreate(BaseModel):
    color_name: str

class ColorOut(BaseModel):
    color_id: int
    color_name: str
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True
