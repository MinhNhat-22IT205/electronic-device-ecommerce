from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class OrderDetailCreate(BaseModel):
    product_price: float = 0.0
    quantity: int = 1
    total_amount: float = 0.0
    order_id: int
    product_id: int

class OrderDetailOut(BaseModel):
    order_detail_id: int
    product_price: float
    quantity: int
    total_amount: float
    order_id: int
    product_id: int
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True