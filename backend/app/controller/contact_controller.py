from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import contact_service
from backend.app.schema.contact_schema import ContactCreate, ContactOut

router = APIRouter(prefix="/contacts", tags=["Contact"])

@router.post("/", response_model=ContactOut)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return contact_service.create_contact(db, contact)

@router.get("/", response_model=list[ContactOut])
def list_contacts(db: Session = Depends(get_db)):
    return contact_service.get_all_contacts(db)

@router.get("/{contact_id}", response_model=ContactOut)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    result = contact_service.get_contact_by_id(db, contact_id)
    if not result:
        raise HTTPException(status_code=404, detail="Contact not found")
    return result

@router.delete("/{contact_id}", response_model=ContactOut)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    result = contact_service.delete_contact(db, contact_id)
    if not result:
        raise HTTPException(status_code=404, detail="Contact not found")
    return result