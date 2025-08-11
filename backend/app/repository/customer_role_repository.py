from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.customer_role import CustomerRole
from backend.app.schema.customerRole_schema import CustomerRoleCreate

def create_customer_role(db: Session, customer_role: CustomerRoleCreate):
    new_customer_role = CustomerRole(
        customer_id=customer_role.customer_id,
        role_id=customer_role.role_id,
        created_at=datetime.utcnow()
    )
    db.add(new_customer_role)
    db.commit()
    db.refresh(new_customer_role)
    return new_customer_role

def get_customer_roles(db: Session):
    return db.query(CustomerRole).filter(CustomerRole.deleted_at == None).all()

def get_customer_role_by_id(db: Session, customer_role_id: int):
    return db.query(CustomerRole).filter(CustomerRole.customer_role_id == customer_role_id).first()