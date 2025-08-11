from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import role_service
from backend.app.schema.role_schema import RoleCreate, RoleOut

router = APIRouter(prefix="/roles", tags=["Role"])

@router.post("/", response_model=RoleOut)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return role_service.create_role(db, role)

@router.get("/", response_model=list[RoleOut])
def list_roles(db: Session = Depends(get_db)):
    return role_service.get_all_roles(db)

@router.get("/{role_id}", response_model=RoleOut)
def get_role(role_id: int, db: Session = Depends(get_db)):
    result = role_service.get_role_by_id(db, role_id)
    if not result:
        raise HTTPException(status_code=404, detail="Role not found")
    return result