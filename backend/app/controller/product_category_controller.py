from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import product_category_service
from backend.app.schema.productCategory_schema import ProductCategoryCreate, ProductCategoryOut

router = APIRouter(prefix="/product_categories", tags=["ProductCategory"])

@router.post("/", response_model=ProductCategoryOut)
def create_product_category(product_category: ProductCategoryCreate, db: Session = Depends(get_db)):
    return product_category_service.create_product_category(db, product_category)

@router.get("/", response_model=list[ProductCategoryOut])
def list_product_categories(db: Session = Depends(get_db)):
    return product_category_service.get_all_product_categories(db)

@router.get("/{product_category_id}", response_model=ProductCategoryOut)
def get_product_category(product_category_id: int, db: Session = Depends(get_db)):
    result = product_category_service.get_product_category_by_id(db, product_category_id)
    if not result:
        raise HTTPException(status_code=404, detail="ProductCategory not found")
    return result

@router.delete("/{product_category_id}", response_model=ProductCategoryOut)
def delete_product_category(product_category_id: int, db: Session = Depends(get_db)):
    result = product_category_service.delete_product_category(db, product_category_id)
    if not result:
        raise HTTPException(status_code=404, detail="ProductCategory not found")
    return result