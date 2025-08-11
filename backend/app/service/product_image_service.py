from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import product_image_repository
from backend.app.schema.productImage_schema import ProductImageCreate

def create_product_image(db: Session, product_image: ProductImageCreate):
    return product_image_repository.create_product_image(db, product_image)

def get_all_product_images(db: Session):
    return product_image_repository.get_product_images(db)

def get_product_image_by_id(db: Session, product_image_id: int):
    return product_image_repository.get_product_image_by_id(db, product_image_id)

def delete_product_image(db: Session, product_image_id: int):
    product_image = product_image_repository.get_product_image_by_id(db, product_image_id)
    if product_image:
        product_image.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(product_image)
    return product_image