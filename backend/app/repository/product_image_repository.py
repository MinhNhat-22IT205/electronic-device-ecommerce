from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.product_image import ProductImage
from backend.app.schema.productImage_schema import ProductImageCreate

def create_product_image(db: Session, product_image: ProductImageCreate):
    new_product_image = ProductImage(
        product_image_path=product_image.product_image_path,
        sort_order=product_image.sort_order,
        product_id=product_image.product_id,
        color_id=product_image.color_id,
        created_at=datetime.utcnow()
    )
    db.add(new_product_image)
    db.commit()
    db.refresh(new_product_image)
    return new_product_image

def get_product_images(db: Session):
    return db.query(ProductImage).filter(ProductImage.deleted_at == None).all()

def get_product_image_by_id(db: Session, product_image_id: int):
    return db.query(ProductImage).filter(ProductImage.product_image_id == product_image_id).first()