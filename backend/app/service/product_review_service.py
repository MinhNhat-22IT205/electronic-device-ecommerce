from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import productReview_repository
from backend.app.schema.productReview_schema import ProductReviewCreate

def create_product_review(db: Session, product_review: ProductReviewCreate):
    return productReview_repository.create_product_review(db, product_review)

def get_all_product_reviews(db: Session):
    return productReview_repository.get_product_reviews(db)

def get_product_review_by_id(db: Session, product_review_id: int):
    return productReview_repository.get_product_review_by_id(db, product_review_id)

def delete_product_review(db: Session, product_review_id: int):
    product_review = productReview_repository.get_product_review_by_id(db, product_review_id)
    if product_review:
        product_review.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(product_review)
    return product_review