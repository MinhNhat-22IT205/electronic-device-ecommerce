from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import orders_repository
from backend.app.schema.orders_schema import OrdersCreate

def create_order(db: Session, order: OrdersCreate):
    return orders_repository.create_order(db, order)

def get_all_orders(db: Session):
    return orders_repository.get_orders(db)

def get_order_by_id(db: Session, order_id: int):
    return orders_repository.get_order_by_id(db, order_id)

def delete_order(db: Session, order_id: int):
    order = orders_repository.get_order_by_id(db, order_id)
    if order:
        order.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(order)
    return order