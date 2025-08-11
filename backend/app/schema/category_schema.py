from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class CategoryCreate(BaseModel):
    category_name: str
    category_image_path: Optional[str] = None
    category_status: Optional[str] = None
    description: Optional[str] = None
    parent_id: Optional[int] = None
    is_activated: bool = True
    is_deleted: bool = False

class CategoryOut(BaseModel):
    category_id: int
    category_name: str
    category_image_path: Optional[str] = None
    category_status: Optional[str] = None
    description: Optional[str] = None
    parent_id: Optional[int] = None
    is_activated: bool
    is_deleted: bool
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True