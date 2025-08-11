from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class AdminRoleCreate(BaseModel):
    admin_id: int
    role_id: int

class AdminRoleOut(BaseModel):
    admin_role_id: int
    admin_id: int
    role_id: int
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True
