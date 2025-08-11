from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import bank_service
from backend.app.schema.bank_schema import BankCreate, BankOut

router = APIRouter(prefix="/banks", tags=["Bank"])

@router.post("/", response_model=BankOut)
def create_bank(bank: BankCreate, db: Session = Depends(get_db)):
    return bank_service.create_bank(db, bank)

@router.get("/", response_model=list[BankOut])
def list_banks(db: Session = Depends(get_db)):
    return bank_service.get_all_banks(db)

@router.get("/{bank_id}", response_model=BankOut)
def get_bank(bank_id: int, db: Session = Depends(get_db)):
    result = bank_service.get_bank_by_id(db, bank_id)
    if not result:
        raise HTTPException(status_code=404, detail="Bank not found")
    return result

@router.delete("/{bank_id}", response_model=BankOut)
def delete_bank(bank_id: int, db: Session = Depends(get_db)):
    result = bank_service.delete_bank(db, bank_id)
    if not result:
        raise HTTPException(status_code=404, detail="Bank not found")
    return result