from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.orders import Orders
from backend.app.schema.orders_schema import OrdersCreate

def create_order(db: Session, order: OrdersCreate):
    new_order = Orders(
        address_1=order.address_1,
        address_2=order.address_2,
        company_name=order.company_name,
        email=order.email,
        first_name=order.first_name,
        last_name=order.last_name,
        order_date=datetime.utcnow(),
        order_note=order.order_note,
        order_status=order.order_status,
        phone=order.phone,
        total_amount=order.total_amount,
        zipcode=order.zipcode,
        city_id=order.city_id,
        customer_id=order.customer_id,
        created_at=datetime.utcnow()
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def get_orders(db: Session):
    return db.query(Orders).filter(Orders.deleted_at == None).all()

def get_order_by_id(db: Session, order_id: int):
    return db.query(Orders).filter(Orders.order_id == order_id).first()