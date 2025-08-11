from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import color_repository
from backend.app.schema.color_schema import ColorCreate

def create_color(db: Session, color: ColorCreate):
    return color_repository.create_color(db, color)

def get_all_colors(db: Session):
    return color_repository.get_colors(db)

def get_color_by_id(db: Session, color_id: int):
    return color_repository.get_color_by_id(db, color_id)

def delete_color(db: Session, color_id: int):
    color = color_repository.get_color_by_id(db, color_id)
    if color:
        color.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(color)
    return color