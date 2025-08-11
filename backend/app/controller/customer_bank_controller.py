from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import customer_bank_service
from backend.app.schema.customerBank_schema import CustomerBankCreate, CustomerBankOut

router = APIRouter(prefix="/customer_banks", tags=["CustomerBank"])

@router.post("/", response_model=CustomerBankOut)
def create_customer_bank(customer_bank: CustomerBankCreate, db: Session = Depends(get_db)):
    return customer_bank_service.create_customer_bank(db, customer_bank)

@router.get("/", response_model=list[CustomerBankOut])
def list_customer_banks(db: Session = Depends(get_db)):
    return customer_bank_service.get_all_customer_banks(db)

@router.get("/{customer_bank_id}", response_model=CustomerBankOut)
def get_customer_bank(customer_bank_id: int, db: Session = Depends(get_db)):
    result = customer_bank_service.get_customer_bank_by_id(db, customer_bank_id)
    if not result:
        raise HTTPException(status_code=404, detail="CustomerBank not found")
    return result

@router.delete("/{customer_bank_id}", response_model=CustomerBankOut)
def delete_customer_bank(customer_bank_id: int, db: Session = Depends(get_db)):
    result = customer_bank_service.delete_customer_bank(db, customer_bank_id)
    if not result:
        raise HTTPException(status_code=404, detail="CustomerBank not found")
    return result