from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.city import City
from backend.app.schema.city_schema import CityCreate

def create_city(db: Session, city: CityCreate):
    new_city = City(
        city_name=city.city_name,
        country_id=city.country_id,
        created_at=datetime.utcnow()
    )
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return new_city

def get_cities(db: Session):
    return db.query(City).filter(City.deleted_at == None).all()

def get_city_by_id(db: Session, city_id: int):
    return db.query(City).filter(City.city_id == city_id).first()