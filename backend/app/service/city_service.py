from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import city_repository
from backend.app.schema.city_schema import CityCreate

def create_city(db: Session, city: CityCreate):
    return city_repository.create_city(db, city)

def get_all_cities(db: Session):
    return city_repository.get_cities(db)

def get_city_by_id(db: Session, city_id: int):
    return city_repository.get_city_by_id(db, city_id)

def delete_city(db: Session, city_id: int):
    city = city_repository.get_city_by_id(db, city_id)
    if city:
        city.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(city)
    return city