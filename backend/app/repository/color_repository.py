from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.color import Color
from backend.app.schema.color_schema import ColorCreate

def create_color(db: Session, color: ColorCreate):
    new_color = Color(
        color_name=color.color_name,
        created_at=datetime.utcnow()
    )
    db.add(new_color)
    db.commit()
    db.refresh(new_color)
    return new_color

def get_colors(db: Session):
    return db.query(Color).filter(Color.deleted_at == None).all()

def get_color_by_id(db: Session, color_id: int):
    return db.query(Color).filter(Color.color_id == color_id).first()