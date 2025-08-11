from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import role_repository
from backend.app.schema.role_schema import RoleCreate

def create_role(db: Session, role: RoleCreate):
    return role_repository.create_role(db, role)

def get_all_roles(db: Session):
    return role_repository.get_roles(db)

def get_role_by_id(db: Session, role_id: int):
    return role_repository.get_role_by_id(db, role_id)

def delete_role(db: Session, role_id: int):
    role = role_repository.get_role_by_id(db, role_id)
    if role:
        role.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(role)
    return role