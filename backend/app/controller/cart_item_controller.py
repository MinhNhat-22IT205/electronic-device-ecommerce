from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import cart_item_service
from backend.app.schema.cartItem_schema import CartItemCreate, CartItemOut

router = APIRouter(prefix="/cart_items", tags=["CartItem"])

@router.post("/", response_model=CartItemOut)
def create_cart_item(cart_item: CartItemCreate, db: Session = Depends(get_db)):
    return cart_item_service.create_cart_item(db, cart_item)

@router.get("/", response_model=list[CartItemOut])
def list_cart_items(db: Session = Depends(get_db)):
    return cart_item_service.get_all_cart_items(db)

@router.get("/{cart_item_id}", response_model=CartItemOut)
def get_cart_item(cart_item_id: int, db: Session = Depends(get_db)):
    result = cart_item_service.get_cart_item_by_id(db, cart_item_id)
    if not result:
        raise HTTPException(status_code=404, detail="CartItem not found")
    return result

@router.delete("/{cart_item_id}", response_model=CartItemOut)
def delete_cart_item(cart_item_id: int, db: Session = Depends(get_db)):
    result = cart_item_service.delete_cart_item(db, cart_item_id)
    if not result:
        raise HTTPException(status_code=404, detail="CartItem not found")
    return result