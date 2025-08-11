from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import customer_bank_repository
from backend.app.schema.customerBank_schema import  CustomerBankCreate

def create_customer_bank(db: Session, customer_bank: CustomerBankCreate):
    return customer_bank_repository.create_customer_bank(db, customer_bank)

def get_all_customer_banks(db: Session):
    return customer_bank_repository.get_customer_banks(db)

def get_customer_bank_by_id(db: Session, customer_bank_id: int):
    return customer_bank_repository.get_customer_bank_by_id(db, customer_bank_id)

def delete_customer_bank(db: Session, customer_bank_id: int):
    customer_bank = customer_bank_repository.get_customer_bank_by_id(db, customer_bank_id)
    if customer_bank:
        customer_bank.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(customer_bank)
    return customer_bank