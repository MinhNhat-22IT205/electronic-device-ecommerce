from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import wishlist_service
from backend.app.schema.wishlist_schema import WishlistCreate, WishlistOut

router = APIRouter(prefix="/wishlists", tags=["Wishlist"])

@router.post("/", response_model=WishlistOut)
def create_wishlist(wishlist: WishlistCreate, db: Session = Depends(get_db)):
    return wishlist_service.create_wishlist(db, wishlist)

@router.get("/", response_model=list[WishlistOut])
def list_wishlists(db: Session = Depends(get_db)):
    return wishlist_service.get_all_wishlists(db)

@router.get("/{wishlist_id}", response_model=WishlistOut)
def get_wishlist(wishlist_id: int, db: Session = Depends(get_db)):
    result = wishlist_service.get_wishlist_by_id(db, wishlist_id)
    if not result:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return result

@router.delete("/{wishlist_id}", response_model=WishlistOut)
def delete_wishlist(wishlist_id: int, db: Session = Depends(get_db)):
    result = wishlist_service.delete_wishlist(db, wishlist_id)
    if not result:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return result