from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import cart_service
from backend.app.schema.cart_schema import CartCreate, CartOut

router = APIRouter(prefix="/carts", tags=["Cart"])

@router.post("/", response_model=CartOut)
def create_cart(cart: CartCreate, db: Session = Depends(get_db)):
    return cart_service.create_cart(db, cart)

@router.get("/", response_model=list[CartOut])
def list_carts(db: Session = Depends(get_db)):
    return cart_service.get_all_carts(db)

@router.get("/{cart_id}", response_model=CartOut)
def get_cart(cart_id: int, db: Session = Depends(get_db)):
    result = cart_service.get_cart_by_id(db, cart_id)
    if not result:
        raise HTTPException(status_code=404, detail="Cart not found")
    return result

@router.delete("/{cart_id}", response_model=CartOut)
def delete_cart(cart_id: int, db: Session = Depends(get_db)):
    result = cart_service.delete_cart(db, cart_id)
    if not result:
        raise HTTPException(status_code=404, detail="Cart not found")
    return result