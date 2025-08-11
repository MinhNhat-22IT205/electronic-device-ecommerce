from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.model.country import Country
from backend.app.schema.country_schema import CountryCreate

def create_country(db: Session, country: CountryCreate):
    new_country = Country(
        country_name=country.country_name,
        created_at=datetime.utcnow()
    )
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country

def get_countries(db: Session):
    return db.query(Country).filter(Country.deleted_at == None).all()

def get_country_by_id(db: Session, country_id: int):
    return db.query(Country).filter(Country.country_id == country_id).first()