from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import color_service
from backend.app.schema.color_schema import ColorCreate, ColorOut

router = APIRouter(prefix="/colors", tags=["Color"])

@router.post("/", response_model=ColorOut)
def create_color(color: ColorCreate, db: Session = Depends(get_db)):
    return color_service.create_color(db, color)

@router.get("/", response_model=list[ColorOut])
def list_colors(db: Session = Depends(get_db)):
    return color_service.get_all_colors(db)

@router.get("/{color_id}", response_model=ColorOut)
def get_color(color_id: int, db: Session = Depends(get_db)):
    result = color_service.get_color_by_id(db, color_id)
    if not result:
        raise HTTPException(status_code=404, detail="Color not found")
    return result

@router.delete("/{color_id}", response_model=ColorOut)
def delete_color(color_id: int, db: Session = Depends(get_db)):
    result = color_service.delete_color(db, color_id)
    if not result:
        raise HTTPException(status_code=404, detail="Color not found")
    return result