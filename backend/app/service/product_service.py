from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import product_repository
from backend.app.schema.product_schema import ProductCreate

def create_product(db: Session, product: ProductCreate):
    return product_repository.create_product(db, product)

def get_all_products(db: Session):
    return product_repository.get_products(db)

def get_product_by_id(db: Session, product_id: int):
    return product_repository.get_product_by_id(db, product_id)

def delete_product(db: Session, product_id: int):
    product = product_repository.get_product_by_id(db, product_id)
    if product:
        product.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(product)
    return product