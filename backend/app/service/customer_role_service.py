from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import customer_role_repository
from backend.app.schema.customerRole_schema import CustomerRoleCreate

def create_customer_role(db: Session, customer_role: CustomerRoleCreate):
    return customer_role_repository.create_customer_role(db, customer_role)

def get_all_customer_roles(db: Session):
    return customer_role_repository.get_customer_roles(db)

def get_customer_role_by_id(db: Session, customer_role_id: int):
    return customer_role_repository.get_customer_role_by_id(db, customer_role_id)

def delete_customer_role(db: Session, customer_role_id: int):
    customer_role = customer_role_repository.get_customer_role_by_id(db, customer_role_id)
    if customer_role:
        customer_role.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(customer_role)
    return customer_role