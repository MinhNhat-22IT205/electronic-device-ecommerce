from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import customer_service
from backend.app.schema.customer_schema import CustomerCreate, CustomerOut

router = APIRouter(prefix="/customers", tags=["Customer"])

@router.post("/", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create_customer(db, customer)

@router.get("/", response_model=list[CustomerOut])
def list_customers(db: Session = Depends(get_db)):
    return customer_service.get_all_customers(db)

@router.get("/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    result = customer_service.get_customer_by_id(db, customer_id)
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    return result