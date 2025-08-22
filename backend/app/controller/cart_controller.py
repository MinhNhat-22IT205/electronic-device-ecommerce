from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.db_session import get_db
from app.schema.cart_schema import CartResponse, CartItemCreate, CartItemResponse, CartItemUpdate
from app.service import cart_service
from app.util.guard import get_current_user

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.get("/", response_model=CartResponse)
def get_user_cart(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return cart_service.get_cart_by_user_service(db, current_user.id)


@router.post("/items", response_model=CartItemResponse)
def add_cart_item(item: CartItemCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return cart_service.add_cart_item_service(db, current_user.id, item)


@router.put("/items/{item_id}", response_model=CartItemResponse)
def update_cart_item(item_id: int, item: CartItemUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return cart_service.update_cart_item_service(db, current_user.id, item_id, item)


@router.delete("/items/{item_id}")
def delete_cart_item(item_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return cart_service.delete_cart_item_service(db, current_user.id, item_id)