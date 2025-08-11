from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import orders_service
from backend.app.schema.orders_schema import OrdersCreate, OrdersOut

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrdersOut)
def create_order(order: OrdersCreate, db: Session = Depends(get_db)):
    return orders_service.create_order(db, order)

@router.get("/", response_model=list[OrdersOut])
def list_orders(db: Session = Depends(get_db)):
    return orders_service.get_all_orders(db)

@router.get("/{order_id}", response_model=OrdersOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    result = orders_service.get_order_by_id(db, order_id)
    if not result:
        raise HTTPException(status_code=404, detail="Order not found")
    return result

@router.delete("/{order_id}", response_model=OrdersOut)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    result = orders_service.delete_order(db, order_id)
    if not result:
        raise HTTPException(status_code=404, detail="Order not found")
    return result