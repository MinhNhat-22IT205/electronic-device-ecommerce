from sqlalchemy.orm import Session
from app.repository.product_repository import get_active_products_with_query, get_product_by_id, create_product
from app.service.minio_service import get_upload_url, get_presigned_url, move_object
from app.config.env_config import env
from app.schema.product_schema import ProductCreateRequest, ProductImageResponse, ProductQueryParams
from app.util.hash import generate_object_key

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
                ProductImageResponse(id=img.id, path=get_presigned_url(env.BUCKET_PRODUCT, img.path))
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

def add_product_and_move_tmp(db, product_data: ProductCreateRequest):
    new_product = create_product(db, product_data)
    for img in product_data.images:
        move_object(env.BUCKET_TMP, env.BUCKET_PRODUCT, img.path, img.path)
    return new_product

def generate_product_upload_url_to_tmp(filename: str):

    object_path = generate_object_key(filename)

    url = get_upload_url(env.BUCKET_TMP, object_path)
    return url, object_path

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
            ProductImageResponse(id=img.id, path=get_presigned_url(env.BUCKET_PRODUCT, img.path))
            for img in product.images
        ],
    }

    return product_dict

