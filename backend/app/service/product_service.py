from sqlalchemy.orm import Session
from app.repository.product_repository import get_active_products

def list_active_products(db: Session):
    return get_active_products(db)