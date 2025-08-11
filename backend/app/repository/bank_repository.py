from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.bank import Bank
from backend.app.schema.bank_schema import BankCreate

def create_bank(db: Session, bank: BankCreate):
    new_bank = Bank(
        bank_name=bank.bank_name,
        created_at=datetime.utcnow()
    )
    db.add(new_bank)
    db.commit()
    db.refresh(new_bank)
    return new_bank

def get_banks(db: Session):
    return db.query(Bank).filter(Bank.deleted_at == None).all()

def get_bank_by_id(db: Session, bank_id: int):
    return db.query(Bank).filter(Bank.bank_id == bank_id).first()