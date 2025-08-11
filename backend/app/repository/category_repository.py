from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.category import Category
from backend.app.schema.category_schema import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    new_category = Category(
        category_name=category.category_name,
        category_image_path=category.category_image_path,
        category_status=category.category_status,
        description=category.description,
        parent_id=category.parent_id,
        is_activated=category.is_activated,
        is_deleted=category.is_deleted,
        created_at=datetime.utcnow()
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_categories(db: Session):
    return db.query(Category).filter(Category.deleted_at == None).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.category_id == category_id).first()