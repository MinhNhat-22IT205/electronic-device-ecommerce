from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import category_service
from backend.app.schema.category_schema import CategoryCreate, CategoryOut

router = APIRouter(prefix="/categories", tags=["Category"])

@router.post("/", response_model=CategoryOut)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.create_category(db, category)

@router.get("/", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return category_service.get_all_categories(db)

@router.get("/{category_id}", response_model=CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    result = category_service.get_category_by_id(db, category_id)
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return result

@router.delete("/{category_id}", response_model=CategoryOut)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    result = category_service.delete_category(db, category_id)
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return result