from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.role import Role
from backend.app.schema.role_schema import RoleCreate

def create_role(db: Session, role: RoleCreate):
    new_role = Role(
        role_name=role.role_name,
        description=role.description,
        created_at=datetime.utcnow()
    )
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def get_roles(db: Session):
    return db.query(Role).filter(Role.deleted_at == None).all()

def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.role_id == role_id).first()