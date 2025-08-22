from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repository import cart_repository
from app.model.product import Product
from app.schema.cart_schema import CartItemCreate, CartItemUpdate, CartItemResponse, CartResponse
from app.service.minio_service import get_presigned_url
from app.config.env_config import env
from app.schema.product_schema import  ProductImageResponse


def get_cart_by_user_service(db: Session, user_id: int):
    cart = cart_repository.get_cart_by_user(db, user_id)
    if not cart:
        cart = cart_repository.create_cart(db, user_id)
        db.commit()
        db.refresh(cart)

    cart_items=[]
    for item in cart.items:
        item_product=item.product
        product_dict = {
            **item_product.__dict__,
            "images": [
                ProductImageResponse(id=img.id, path=get_presigned_url(env.BUCKET_PRODUCT, img.path))
                for img in item_product.images
            ]
        }
        cart_items.append(
            CartItemResponse(
                id=item.id,
                product=product_dict,
                quantity=item.quantity,
                total_price=item.total_price,
                product_price=item.product_price
            )
        )
    return CartResponse(
        id=cart.id,
        user_id=cart.user_id,
        total_amount=cart.total_amount,
        total_item=cart.total_item,
        items=cart_items,
    )


def add_cart_item_service(db: Session, user_id: int, item_data: CartItemCreate):
    cart = get_cart_by_user_service(db, user_id)

    product = db.query(Product).filter(Product.id == item_data.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_item = cart_repository.get_cart_item_by_product(db, cart.id, product.id)

    if existing_item:
        existing_item.quantity += item_data.quantity
        existing_item.total_price = existing_item.product_price * existing_item.quantity
    else:
        existing_item = cart_repository.add_cart_item(db, cart.id, product, item_data.quantity)

    # recalc totals
    cart.total_amount = sum(i.total_price for i in cart.items)
    cart.total_item = sum(i.quantity for i in cart.items)

    db.commit()
    db.refresh(existing_item)
    return existing_item


def update_cart_item_service(db: Session, user_id: int, item_id: int, item_data: CartItemUpdate):
    cart = get_cart_by_user_service(db, user_id)
    cart_item = cart_repository.get_cart_item(db, item_id)

    if not cart_item or cart_item.cart_id != cart.id:
        raise HTTPException(status_code=404, detail="Cart item not found")

    product = db.query(Product).filter(Product.id == cart_item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    cart_item.quantity = max(0, item_data.quantity)
    cart_item.total_price = product.sale_price * cart_item.quantity

    cart.total_amount = sum(i.total_price for i in cart.items)
    cart.total_item = sum(i.quantity for i in cart.items)

    db.commit()
    db.refresh(cart_item)
    return cart_item


def delete_cart_item_service(db: Session, user_id: int, item_id: int):
    cart = get_cart_by_user_service(db, user_id)
    cart_item = cart_repository.get_cart_item(db, item_id)

    if not cart_item or cart_item.cart_id != cart.id:
        raise HTTPException(status_code=404, detail="Cart item not found")

    db.delete(cart_item)

    cart.total_amount = sum(i.total_price for i in cart.items if i.id != item_id)
    cart.total_item = sum(i.quantity for i in cart.items if i.id != item_id)

    db.commit()
    return {"message": "Cart item deleted successfully"}
