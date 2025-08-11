from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.product_review import ProductReview
from backend.app.schema.productReview_schema import ProductReviewCreate

def create_product_review(db: Session, product_review: ProductReviewCreate):
    new_product_review = ProductReview(
        comment=product_review.comment,
        rating=product_review.rating,
        num_comment=product_review.num_comment,
        customer_id=product_review.customer_id,
        product_id=product_review.product_id,
        created_at=datetime.utcnow()
    )
    db.add(new_product_review)
    db.commit()
    db.refresh(new_product_review)
    return new_product_review

def get_product_reviews(db: Session):
    return db.query(ProductReview).filter(ProductReview.deleted_at == None).all()

def get_product_review_by_id(db: Session, product_review_id: int):
    return db.query(ProductReview).filter(ProductReview.product_review_id == product_review_id).first()