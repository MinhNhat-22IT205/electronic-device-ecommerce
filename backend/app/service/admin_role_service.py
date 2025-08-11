from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import admin_role_repository
from backend.app.schema.adminrole_schema import AdminRoleCreate

def create_admin_role(db: Session, admin_role: AdminRoleCreate):
    return admin_role_repository.create_admin_role(db, admin_role)

def get_all_admin_roles(db: Session):
    return admin_role_repository.get_admin_roles(db)

def get_admin_role_by_id(db: Session, admin_role_id: int):
    return admin_role_repository.get_admin_role_by_id(db, admin_role_id)

def delete_admin_role(db: Session, admin_role_id: int):
    admin_role = admin_role_repository.get_admin_role_by_id(db, admin_role_id)
    if admin_role:
        admin_role.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(admin_role)
    return admin_role