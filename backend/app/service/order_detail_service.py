from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import order_detail_repository
from backend.app.schema.orderDetail_schema import  OrderDetailCreate

def create_order_detail(db: Session, order_detail: OrderDetailCreate):
    return order_detail_repository.create_order_detail(db, order_detail)

def get_all_order_details(db: Session):
    return order_detail_repository.get_order_details(db)

def get_order_detail_by_id(db: Session, order_detail_id: int):
    return order_detail_repository.get_order_detail_by_id(db, order_detail_id)

def delete_order_detail(db: Session, order_detail_id: int):
    order_detail = order_detail_repository.get_order_detail_by_id(db, order_detail_id)
    if order_detail:
        order_detail.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(order_detail)
    return order_detail