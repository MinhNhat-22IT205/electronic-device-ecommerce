from sqlalchemy.orm import Session
from app.model.product import Product
from app.model.product_image import ProductImage
from app.schema.product_schema import ProductCreateRequest, ProductQueryParams

def get_active_products_with_query(db: Session, params: ProductQueryParams):
    query = db.query(Product).filter(Product.is_activated == True)

    # Search
    if params.search:
        query = query.filter(Product.name.ilike(f"%{params.search}%"))

    # Sorting
    if params.sort == "price_low":
        query = query.order_by(Product.sale_price.desc())
    elif params.sort == "price_high":
        query = query.order_by(Product.sale_price.asc())
    else:  # newest
        query = query.order_by(Product.created_at.desc())

    # Pagination
    total = query.count()
    products = query.offset((params.page - 1) * params.limit).limit(params.limit).all()
    return products, total

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product_data: ProductCreateRequest):
    data = product_data.model_dump(exclude={"images"})

    product = Product(
        **data,
        is_activated=True,
        images=[ProductImage(path=img.path) for img in product_data.images]
    )

    db.add(product)
    db.commit()
    db.refresh(product)  # product.images will now be loaded

    return product