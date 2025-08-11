from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class CartCreate(BaseModel):
    total_amount: float = 0.0
    total_item: int = 0
    customer_id: int

class CartOut(BaseModel):
    cart_id: int
    total_amount: float
    total_item: int
    customer_id: int
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True
