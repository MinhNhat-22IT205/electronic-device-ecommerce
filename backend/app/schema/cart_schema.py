from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.schema.product_schema import ProductResponse


class CartItemBase(BaseModel):
    product_id: int
    quantity: int


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    quantity: int


class CartItemResponse(BaseModel):
    id: int
    quantity: int
    product_price: float
    total_price: float
    product: ProductResponse   # nested product info

    class Config:
        orm_mode = True


class CartResponse(BaseModel):
    id: int
    user_id: Optional[int]
    total_amount: float
    total_item: int
    items: List[CartItemResponse]

    class Config:
        orm_mode = True
