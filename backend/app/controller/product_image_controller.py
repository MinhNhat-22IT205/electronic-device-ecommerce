from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import product_image_service
from backend.app.schema.productImage_schema import ProductImageCreate, ProductImageOut

router = APIRouter(prefix="/product_images", tags=["ProductImage"])

@router.post("/", response_model=ProductImageOut)
def create_product_image(product_image: ProductImageCreate, db: Session = Depends(get_db)):
    return product_image_service.create_product_image(db, product_image)

@router.get("/", response_model=list[ProductImageOut])
def list_product_images(db: Session = Depends(get_db)):
    return product_image_service.get_all_product_images(db)

@router.get("/{product_image_id}", response_model=ProductImageOut)
def get_product_image(product_image_id: int, db: Session = Depends(get_db)):
    result = product_image_service.get_product_image_by_id(db, product_image_id)
    if not result:
        raise HTTPException(status_code=404, detail="ProductImage not found")
    return result

@router.delete("/{product_image_id}", response_model=ProductImageOut)
def delete_product_image(product_image_id: int, db: Session = Depends(get_db)):
    result = product_image_service.delete_product_image(db, product_image_id)
    if not result:
        raise HTTPException(status_code=404, detail="ProductImage not found")
    return result