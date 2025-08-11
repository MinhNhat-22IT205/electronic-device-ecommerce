from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import product_review_service
from backend.app.schema.productReview_schema import ProductReviewCreate, ProductReviewOut

router = APIRouter(prefix="/product_reviews", tags=["ProductReview"])

@router.post("/", response_model=ProductReviewOut)
def create_product_review(product_review: ProductReviewCreate, db: Session = Depends(get_db)):
    return product_review_service.create_product_review(db, product_review)

@router.get("/", response_model=list[ProductReviewOut])
def list_product_reviews(db: Session = Depends(get_db)):
    return product_review_service.get_all_product_reviews(db)

@router.get("/{product_review_id}", response_model=ProductReviewOut)
def get_product_review(product_review_id: int, db: Session = Depends(get_db)):
    result = product_review_service.get_product_review_by_id(db, product_review_id)
    if not result:
        raise HTTPException(status_code=404, detail="ProductReview not found")
    return result

@router.delete("/{product_review_id}", response_model=ProductReviewOut)
def delete_product_review(product_review_id: int, db: Session = Depends(get_db)):
    result = product_review_service.delete_product_review(db, product_review_id)
    if not result:
        raise HTTPException(status_code=404, detail="ProductReview not found")
    return result