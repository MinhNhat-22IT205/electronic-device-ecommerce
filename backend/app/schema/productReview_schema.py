from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class ProductReviewCreate(BaseModel):
    comment: Optional[str] = None
    rating: int
    num_comment: int = 0
    customer_id: int
    product_id: int

class ProductReviewOut(BaseModel):
    product_review_id: int
    comment: Optional[str] = None
    rating: int
    num_comment: int
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