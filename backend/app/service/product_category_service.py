from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import product_category_repository
from backend.app.schema.productCategory_schema import  ProductCategoryCreate

def create_product_category(db: Session, product_category: ProductCategoryCreate):
    return product_category_repository.create_product_category(db, product_category)

def get_all_product_categories(db: Session):
    return product_category_repository.get_product_categories(db)

def get_product_category_by_id(db: Session, product_category_id: int):
    return product_category_repository.get_product_category_by_id(db, product_category_id)

def delete_product_category(db: Session, product_category_id: int):
    product_category = product_category_repository.get_product_category_by_id(db, product_category_id)
    if product_category:
        product_category.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(product_category)
    return product_category