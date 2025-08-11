from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.repository import country_repository
from backend.app.schema.country_schema import CountryCreate

def create_country(db: Session, country: CountryCreate):
    return country_repository.create_country(db, country)

def get_all_countries(db: Session):
    return country_repository.get_countries(db)

def get_country_by_id(db: Session, country_id: int):
    return country_repository.get_country_by_id(db, country_id)

def delete_country(db: Session, country_id: int):
    country = country_repository.get_country_by_id(db, country_id)
    if country:
        country.deleted_at = datetime.utcnow()
        db.commit()
        db.refresh(country)
    return country