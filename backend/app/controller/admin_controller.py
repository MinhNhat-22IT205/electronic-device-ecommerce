from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import admin_service
from backend.app.schema.admin_schema import AdminCreate, AdminOut

router = APIRouter(prefix="/admins", tags=["Admin"])

@router.post("/", response_model=AdminOut)
def create_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    return admin_service.create_admin(db, admin)

@router.get("/", response_model=list[AdminOut])
def list_admins(db: Session = Depends(get_db)):
    return admin_service.get_all_admins(db)

@router.get("/{admin_id}", response_model=AdminOut)
def get_admin(admin_id: int, db: Session = Depends(get_db)):
    result = admin_service.get_admin_by_id(admin_id, db)
    if not result:
        raise HTTPException(status_code=404, detail="Admin not found")
    return result
