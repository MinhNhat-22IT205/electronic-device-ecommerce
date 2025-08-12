from sqlalchemy.orm import Session
from app.repository.product_repository import get_active_products_with_query, save_product_image, get_product_by_id, create_product
from app.service.minio_service import get_upload_url, get_presigned_url
from app.config.env_config import env
from app.schema.product_schema import ProductCreateRequest, ProductImageResponse, ProductQueryParams

def list_active_products_with_query(db: Session, params: ProductQueryParams):
    products, total =  get_active_products_with_query(db, params)
    product_list = []

    for product in products:
        product_dict = {
            **product.__dict__,
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "images": [
                ProductImageResponse(id=img.id, path=get_presigned_url(img.bucket_name, img.object_key))
                for img in product.images
            ]
        }

        product_list.append(product_dict)

    return {
        "data": product_list,
        "pagination": {
            "page": params.page,
            "limit": params.limit,
            "total": total,
            "pages": (total + params.limit - 1) // params.limit
        }
    }

def add_product(db, product_data: ProductCreateRequest):
    return create_product(db, product_data)

def generate_product_upload_url(db: Session, product_id: int, filename: str):
    product = get_product_by_id(db, product_id)
    if not product:
        raise ValueError("Product not found")

    object_path = f"{product_id}/{filename}"

    url = get_upload_url(env.BUCKET_PRODUCT, object_path)
    return url, object_path

def save_uploaded_image(db: Session, product_id: int, bucket_name: str, object_key:str):
    return save_product_image(db, product_id, bucket_name, object_key)

def get_product_detail(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if not product:
        return None

    # Convert to dict and add presigned URLs for images
    product_dict = {
        **product.__dict__,
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "images": [
            ProductImageResponse(id=img.id, path=get_presigned_url(img.bucket_name, img.object_key))
            for img in product.images
        ],
    }

    return product_dict

