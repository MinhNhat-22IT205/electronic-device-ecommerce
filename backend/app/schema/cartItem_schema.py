from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class CartItemCreate(BaseModel):
    cart_item_sku: str
    product_price: float = 0.0
    quantity: int = 1
    total_price: float = 0.0
    cart_id: int
    product_id: int

class CartItemOut(BaseModel):
    cart_item_id: int
    cart_item_sku: str
    product_price: float
    quantity: int
    total_price: float
    cart_id: int
    product_id: int
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True