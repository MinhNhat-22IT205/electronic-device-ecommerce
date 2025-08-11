from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import wishlist_repository
from backend.app.schema.wishlist_schema import WishlistCreate

def create_wishlist(db: Session, wishlist: WishlistCreate):
    return wishlist_repository.create_wishlist(db, wishlist)

def get_all_wishlists(db: Session):
    return wishlist_repository.get_wishlists(db)

def get_wishlist_by_id(db: Session, wishlist_id: int):
    return wishlist_repository.get_wishlist_by_id(db, wishlist_id)

def delete_wishlist(db: Session, wishlist_id: int):
    wishlist = wishlist_repository.get_wishlist_by_id(db, wishlist_id)
    if wishlist:
        wishlist.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(wishlist)
    return wishlist