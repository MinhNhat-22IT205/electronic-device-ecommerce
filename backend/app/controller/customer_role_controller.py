from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import customer_role_service
from backend.app.schema.customerRole_schema import CustomerRoleCreate, CustomerRoleOut

router = APIRouter(prefix="/customer_roles", tags=["CustomerRole"])

@router.post("/", response_model=CustomerRoleOut)
def create_customer_role(customer_role: CustomerRoleCreate, db: Session = Depends(get_db)):
    return customer_role_service.create_customer_role(db, customer_role)

@router.get("/", response_model=list[CustomerRoleOut])
def list_customer_roles(db: Session = Depends(get_db)):
    return customer_role_service.get_all_customer_roles(db)

@router.get("/{customer_role_id}", response_model=CustomerRoleOut)
def get_customer_role(customer_role_id: int, db: Session = Depends(get_db)):
    result = customer_role_service.get_customer_role_by_id(db, customer_role_id)
    if not result:
        raise HTTPException(status_code=404, detail="CustomerRole not found")
    return result