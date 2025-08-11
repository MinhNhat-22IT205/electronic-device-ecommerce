from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import bank_repository
from backend.app.schema.bank_schema import BankCreate

def create_bank(db: Session, bank: BankCreate):
    return bank_repository.create_bank(db, bank)

def get_all_banks(db: Session):
    return bank_repository.get_banks(db)

def get_bank_by_id(db: Session, bank_id: int):
    return bank_repository.get_bank_by_id(db, bank_id)

def delete_bank(db: Session, bank_id: int):
    bank = bank_repository.get_bank_by_id(db, bank_id)
    if bank:
        bank.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(bank)
    return bank