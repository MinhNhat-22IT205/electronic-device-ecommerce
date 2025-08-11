from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.customer_bank import CustomerBank
from backend.app.schema.customerBank_schema import CustomerBankCreate

def create_customer_bank(db: Session, customer_bank: CustomerBankCreate):
    new_customer_bank = CustomerBank(
        bank_account_number=customer_bank.bank_account_number,
        bank_id=customer_bank.bank_id,
        customer_id=customer_bank.customer_id,
        created_at=datetime.utcnow()
    )
    db.add(new_customer_bank)
    db.commit()
    db.refresh(new_customer_bank)
    return new_customer_bank

def get_customer_banks(db: Session):
    return db.query(CustomerBank).filter(CustomerBank.deleted_at == None).all()

def get_customer_bank_by_id(db: Session, customer_bank_id: int):
    return db.query(CustomerBank).filter(CustomerBank.customer_bank_id == customer_bank_id).first()