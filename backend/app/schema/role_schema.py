from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class RoleCreate(BaseModel):
    role_name: str
    description: Optional[str] = None

class RoleOut(BaseModel):
    role_id: int
    role_name: str
    description: Optional[str] = None
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True
