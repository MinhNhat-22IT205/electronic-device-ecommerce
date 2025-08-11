from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.contact import Contact
from backend.app.schema.contact_schema import ContactCreate

def create_contact(db: Session, contact: ContactCreate):
    new_contact = Contact(
        email=contact.email,
        message=contact.message,
        name=contact.name,
        subject=contact.subject,
        customer_id=contact.customer_id,
        created_at=datetime.utcnow()
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

def get_contacts(db: Session):
    return db.query(Contact).filter(Contact.deleted_at == None).all()

def get_contact_by_id(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.contact_id == contact_id).first()