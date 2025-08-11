from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class ProductCreate(BaseModel):
    product_name: str
    product_sku: str
    description: Optional[str] = None
    camera: Optional[str] = None
    cpu: Optional[str] = None
    ram: Optional[int] = None
    rom: Optional[int] = None
    pin: Optional[int] = None
    cost_price: float = 0.0
    sale_price: float = 0.0
    current_quantity: int = 0
    weight: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
    thick: Optional[float] = None
    is_activated: bool = True
    is_deleted: bool = False

class ProductOut(BaseModel):
    product_id: int
    product_name: str
    product_sku: str
    description: Optional[str] = None
    camera: Optional[str] = None
    cpu: Optional[str] = None
    ram: Optional[int] = None
    rom: Optional[int] = None
    pin: Optional[int] = None
    cost_price: float
    sale_price: float
    current_quantity: int
    weight: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
    thick: Optional[float] = None
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