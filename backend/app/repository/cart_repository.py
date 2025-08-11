from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.cart import Cart
from backend.app.schema.cart_schema import CartCreate

def create_cart(db: Session, cart: CartCreate):
    new_cart = Cart(
        total_amount=cart.total_amount,
        total_item=cart.total_item,
        customer_id=cart.customer_id,
        created_at=datetime.utcnow()
    )
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart

def get_carts(db: Session):
    return db.query(Cart).filter(Cart.deleted_at == None).all()

def get_cart_by_id(db: Session, cart_id: int):
    return db.query(Cart).filter(Cart.cart_id == cart_id).first()