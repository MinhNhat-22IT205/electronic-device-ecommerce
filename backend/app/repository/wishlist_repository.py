from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.wishlist import Wishlist
from backend.app.schema.wishlist_schema import WishlistCreate

def create_wishlist(db: Session, wishlist: WishlistCreate):
    new_wishlist = Wishlist(
        customer_id=wishlist.customer_id,
        product_id=wishlist.product_id,
        created_at=datetime.utcnow()
    )
    db.add(new_wishlist)
    db.commit()
    db.refresh(new_wishlist)
    return new_wishlist

def get_wishlists(db: Session):
    return db.query(Wishlist).filter(Wishlist.deleted_at == None).all()

def get_wishlist_by_id(db: Session, wishlist_id: int):
    return db.query(Wishlist).filter(Wishlist.wishlist_id == wishlist_id).first()