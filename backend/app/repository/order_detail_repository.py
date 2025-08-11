from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.order_detail import OrderDetail
from backend.app.schema.orderDetail_schema import OrderDetailCreate

def create_order_detail(db: Session, order_detail: OrderDetailCreate):
    new_order_detail = OrderDetail(
        product_price=order_detail.product_price,
        quantity=order_detail.quantity,
        total_amount=order_detail.total_amount,
        order_id=order_detail.order_id,
        product_id=order_detail.product_id,
        created_at=datetime.utcnow()
    )
    db.add(new_order_detail)
    db.commit()
    db.refresh(new_order_detail)
    return new_order_detail

def get_order_details(db: Session):
    return db.query(OrderDetail).filter(OrderDetail.deleted_at == None).all()

def get_order_detail_by_id(db: Session, order_detail_id: int):
    return db.query(OrderDetail).filter(OrderDetail.order_detail_id == order_detail_id).first()