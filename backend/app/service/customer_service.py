from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import customer_repository
from backend.app.schema.customer_schema import CustomerCreate

def create_customer(db: Session, customer: CustomerCreate):
    return customer_repository.create_customer(db, customer)

def get_all_customers(db: Session):
    return customer_repository.get_customers(db)

def get_customer_by_id(db: Session, customer_id: int):
    return customer_repository.get_customer_by_id(db, customer_id)

def delete_customer(db: Session, customer_id: int):
    customer = customer_repository.get_customer_by_id(db, customer_id)
    if customer:
        customer.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(customer)
    return customer