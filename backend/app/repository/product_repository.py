from sqlalchemy.orm import Session
from app.model.product import Product
from app.model.product_image import ProductImage
from app.schema.product_schema import ProductCreateRequest, ProductQueryParams, ProductPatchRequest
from fastapi import HTTPException
from datetime import datetime, timezone

def get_active_products_with_query(db: Session, params: ProductQueryParams):
    query = db.query(Product).filter(Product.is_activated == True, Product.is_deleted == False)

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

def patch_product(db: Session, product: Product, patch_data: ProductPatchRequest):
    # Only update fields provided by client
    update_data = patch_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        if key == "images":
            # Clear existing images and replace with new ones
            product.images.clear()
            for img_data in value:
                product.images.append(ProductImage(**img_data))
        else:
            setattr(product, key, value)

    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def mark_product_as_deleted(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Soft delete instead of hard delete
    product.is_deleted = True
    product.is_activated = False
    product.deleted_at = datetime.now(timezone.utc)

    db.add(product)
    db.commit()
    db.refresh(product)

    return product