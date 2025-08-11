from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class ProductImageCreate(BaseModel):
    product_image_path: str
    sort_order: int = 0
    product_id: int
    color_id: int

class ProductImageOut(BaseModel):
    product_image_id: int
    product_image_path: str
    sort_order: int
    product_id: int
    color_id: int
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True
