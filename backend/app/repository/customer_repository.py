from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.customer import Customer
from backend.app.schema.customer_schema import CustomerCreate

def create_customer(db: Session, customer: CustomerCreate):
    new_customer = Customer(
        customeremail=customer.customeremail,
        customerpassword=customer.customerpassword,
        customer_phone=customer.customer_phone,
        first_name=customer.first_name,
        last_name=customer.last_name,
        country_id=customer.country_id,
        registration_date=datetime.utcnow(),
        created_at=datetime.utcnow()
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def get_customers(db: Session):
    return db.query(Customer).filter(Customer.deleted_at == None).all()

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.customer_id == customer_id).first()