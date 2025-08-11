from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import order_detail_service
from backend.app.schema.orderDetail_schema import  OrderDetailCreate, OrderDetailOut

router = APIRouter(prefix="/order_details", tags=["OrderDetail"])

@router.post("/", response_model=OrderDetailOut)
def create_order_detail(order_detail: OrderDetailCreate, db: Session = Depends(get_db)):
    return order_detail_service.create_order_detail(db, order_detail)

@router.get("/", response_model=list[OrderDetailOut])
def list_order_details(db: Session = Depends(get_db)):
    return order_detail_service.get_all_order_details(db)

@router.get("/{order_detail_id}", response_model=OrderDetailOut)
def get_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    result = order_detail_service.get_order_detail_by_id(db, order_detail_id)
    if not result:
        raise HTTPException(status_code=404, detail="OrderDetail not found")
    return result

@router.delete("/{order_detail_id}", response_model=OrderDetailOut)
def delete_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    result = order_detail_service.delete_order_detail(db, order_detail_id)
    if not result:
        raise HTTPException(status_code=404, detail="OrderDetail not found")
    return result