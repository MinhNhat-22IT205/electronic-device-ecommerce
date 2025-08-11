from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.product_category import ProductCategory
from backend.app.schema.productCategory_schema import ProductCategoryCreate

def create_product_category(db: Session, product_category: ProductCategoryCreate):
    new_product_category = ProductCategory(
        product_id=product_category.product_id,
        category_id=product_category.category_id,
        created_at=datetime.utcnow()
    )
    db.add(new_product_category)
    db.commit()
    db.refresh(new_product_category)
    return new_product_category

def get_product_categories(db: Session):
    return db.query(ProductCategory).filter(ProductCategory.deleted_at == None).all()

def get_product_category_by_id(db: Session, product_category_id: int):
    return db.query(ProductCategory).filter(ProductCategory.product_category_id == product_category_id).first()