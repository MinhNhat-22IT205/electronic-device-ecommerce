from sqlalchemy.orm import Session
from backend.app.repository import admin_repository
from backend.app.schema.admin_schema import AdminCreate

def create_admin(db: Session, admin: AdminCreate):
    return admin_repository.create_admin(db, admin)

def get_all_admins(db: Session):
    return admin_repository.get_admins(db)

def get_admin_by_id(db: Session, admin_id: int):
    return admin_repository.get_admin_by_id(db, admin_id)
