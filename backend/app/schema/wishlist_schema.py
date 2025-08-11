from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class WishlistCreate(BaseModel):
    customer_id: int
    product_id: int

class WishlistOut(BaseModel):
    wishlist_id: int
    customer_id: int
    product_id: int
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True