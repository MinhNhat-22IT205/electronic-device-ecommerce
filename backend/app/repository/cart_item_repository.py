from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.cart_item import CartItem
from backend.app.schema.cartItem_schema import CartItemCreate

def create_cart_item(db: Session, cart_item: CartItemCreate):
    new_cart_item = CartItem(
        cart_item_sku=cart_item.cart_item_sku,
        product_price=cart_item.product_price,
        quantity=cart_item.quantity,
        total_price=cart_item.total_price,
        cart_id=cart_item.cart_id,
        product_id=cart_item.product_id,
        created_at=datetime.utcnow()
    )
    db.add(new_cart_item)
    db.commit()
    db.refresh(new_cart_item)
    return new_cart_item

def get_cart_items(db: Session):
    return db.query(CartItem).filter(CartItem.deleted_at == None).all()

def get_cart_item_by_id(db: Session, cart_item_id: int):
    return db.query(CartItem).filter(CartItem.cart_item_id == cart_item_id).first()