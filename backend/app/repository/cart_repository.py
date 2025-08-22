from sqlalchemy.orm import Session
from app.model.cart import Cart
from app.model.cart_item import CartItem
from app.model.product import Product


def create_cart(db: Session, user_id: int) -> Cart:
    cart = Cart(user_id=user_id, total_amount=0, total_item=0)
    db.add(cart)
    db.flush()
    return cart


def get_cart_by_user(db: Session, user_id: int) -> Cart:
    return db.query(Cart).filter(Cart.user_id == user_id).first()


def add_cart_item(db: Session, cart_id: int, product: Product, quantity: int) -> CartItem:
    total_price = product.sale_price * quantity
    cart_item = CartItem(
        cart_id=cart_id,
        product_id=product.id,
        product_price=product.sale_price,
        quantity=quantity,
        total_price=total_price,
    )
    db.add(cart_item)
    db.flush()
    return cart_item


def get_cart_item(db: Session, item_id: int) -> CartItem:
    return db.query(CartItem).filter(CartItem.id == item_id).first()


def get_cart_item_by_product(db: Session, cart_id: int, product_id: int) -> CartItem:
    return db.query(CartItem).filter(
        CartItem.cart_id == cart_id,
        CartItem.product_id == product_id
    ).first()
