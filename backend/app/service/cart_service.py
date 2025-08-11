from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import cart_repository
from backend.app.schema.cart_schema import CartCreate

def create_cart(db: Session, cart: CartCreate):
    return cart_repository.create_cart(db, cart)

def get_all_carts(db: Session):
    return cart_repository.get_carts(db)

def get_cart_by_id(db: Session, cart_id: int):
    return cart_repository.get_cart_by_id(db, cart_id)

def delete_cart(db: Session, cart_id: int):
    cart = cart_repository.get_cart_by_id(db, cart_id)
    if cart:
        cart.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(cart)
    return cart