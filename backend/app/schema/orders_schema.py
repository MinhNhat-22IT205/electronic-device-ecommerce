from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class OrdersCreate(BaseModel):
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    company_name: Optional[str] = None
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    order_note: Optional[str] = None
    order_status: str
    phone: Optional[str] = None
    total_amount: float = 0.0
    zipcode: Optional[str] = None
    city_id: int
    customer_id: int

class OrdersOut(BaseModel):
    order_id: int
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    company_name: Optional[str] = None
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    order_date: Optional[datetime] = None
    order_note: Optional[str] = None
    order_status: str
    phone: Optional[str] = None
    total_amount: float
    zipcode: Optional[str] = None
    city_id: int
    customer_id: int
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True