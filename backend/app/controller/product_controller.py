from fastapi import APIRouter, Depends, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schema.product_schema import ProductResponse, ProductCreateResponse, ProductQueryParams, ProductListResponse, ProductCreateRequest
from app.db.db_session import get_db
from app.util.guard import admin_required
from app.service.product_service import list_active_products_with_query, save_uploaded_image, generate_product_upload_url, get_product_detail, add_product
from app.config.env_config import env
from fastapi import Form

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=ProductListResponse)
def list_products(params: ProductQueryParams = Depends(),db: Session = Depends(get_db)):
    return list_active_products_with_query(db, params )

@router.post("/", response_model=ProductCreateResponse)
def create_product(product_data: ProductCreateRequest,current_user = Depends(admin_required), db: Session = Depends(get_db)):
    
    print(product_data)
    new_product = add_product(db, product_data)
    return new_product

@router.get("/{product_id}/get-upload-url")
def get_product_upload_url( product_id: str, filename: str,current_user = Depends(admin_required), db: Session = Depends(get_db)):
    #get upload presigned url
    url, object_path = generate_product_upload_url(db, product_id, filename)

    return {
        "upload_url": url,
        "object_path": object_path
    }

@router.post("/{product_id}/save-image")
def save_product_image(product_id: int, object_path: str,current_user = Depends(admin_required), db: Session = Depends(get_db)):
    #save to db
    product_image = save_uploaded_image(db, product_id,env.BUCKET_PRODUCT,object_path)
    if not product_image:
        raise HTTPException(status_code=400, detail="image not saved")
    return product_image

@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id_api(product_id: int, db: Session = Depends(get_db)):
    product = get_product_detail(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product