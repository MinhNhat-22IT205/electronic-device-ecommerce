
from pydantic import BaseModel
from typing import List, Optional

class ProductImageResponse(BaseModel):
    path: str
    color: str

    class Config:
        orm_mode = True

class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    sale_price: float
    current_quantity: int
    is_activated: bool
    images: List[ProductImageResponse]

    class Config:
        orm_mode = True
