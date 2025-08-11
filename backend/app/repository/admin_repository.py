from sqlalchemy.orm import Session
from datetime import datetime

from backend.app.model.admin import Admin
from backend.app.schema.admin_schema import AdminCreate


def create_admin(db: Session, admin: AdminCreate):
    new_admin = Admin(
        email=admin.email,
        first_name=admin.first_name,
        last_name=admin.last_name,
        password=admin.password,
        registration_date=datetime.utcnow(),
        created_at=datetime.utcnow()
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

def get_admins(db: Session):
    return db.query(Admin).filter(Admin.deleted_at == None).all()

def get_admin_by_id(db: Session, admin_id: int):
    return db.query(Admin).filter(Admin.admin_id == admin_id).first()
