from sqlalchemy.orm import Session
from app.model.product import Product

def get_active_products(db: Session):
    return db.query(Product).filter(Product.is_activated == True).all()