from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.admin_role import AdminRole
from backend.app.schema.adminrole_schema import AdminRoleCreate

def create_admin_role(db: Session, admin_role: AdminRoleCreate):
    new_admin_role = AdminRole(
        admin_id=admin_role.admin_id,
        role_id=admin_role.role_id,
        created_at=datetime.utcnow()
    )
    db.add(new_admin_role)
    db.commit()
    db.refresh(new_admin_role)
    return new_admin_role

def get_admin_roles(db: Session):
    return db.query(AdminRole).filter(AdminRole.deleted_at == None).all()

def get_admin_role_by_id(db: Session, admin_role_id: int):
    return db.query(AdminRole).filter(AdminRole.admin_role_id == admin_role_id).first()