from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schema.product_schema import ProductResponse
from app.db.db_session import get_db
from app.service.product_service import list_active_products

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return list_active_products(db)
