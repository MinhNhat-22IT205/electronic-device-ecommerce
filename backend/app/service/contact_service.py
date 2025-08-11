from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import contact_repository
from backend.app.schema.contact_schema import ContactCreate

def create_contact(db: Session, contact: ContactCreate):
    return contact_repository.create_contact(db, contact)

def get_all_contacts(db: Session):
    return contact_repository.get_contacts(db)

def get_contact_by_id(db: Session, contact_id: int):
    return contact_repository.get_contact_by_id(db, contact_id)

def delete_contact(db: Session, contact_id: int):
    contact = contact_repository.get_contact_by_id(db, contact_id)
    if contact:
        contact.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(contact)
    return contact