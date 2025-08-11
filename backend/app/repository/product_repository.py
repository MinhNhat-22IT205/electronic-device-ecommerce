from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.product import Product
from backend.app.schema.product_schema import ProductCreate

def create_product(db: Session, product: ProductCreate):
    new_product = Product(
        product_name=product.product_name,
        product_sku=product.product_sku,
        description=product.description,
        camera=product.camera,
        cpu=product.cpu,
        ram=product.ram,
        rom=product.rom,
        pin=product.pin,
        cost_price=product.cost_price,
        sale_price=product.sale_price,
        current_quantity=product.current_quantity,
        weight=product.weight,
        width=product.width,
        height=product.height,
        thick=product.thick,
        is_activated=product.is_activated,
        is_deleted=product.is_deleted,
        created_at=datetime.utcnow()
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_products(db: Session):
    return db.query(Product).filter(Product.deleted_at == None).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.product_id == product_id).first()