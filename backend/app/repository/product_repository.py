from sqlalchemy.orm import Session
from app.model.product import Product
from app.schema.product_schema import ProductImageResponse, ProductResponse

def get_active_products(db: Session):
    products = db.query(Product).filter(Product.is_activated == True).all()

    return products
