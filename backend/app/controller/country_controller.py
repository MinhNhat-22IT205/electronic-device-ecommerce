from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import country_service
from backend.app.schema.country_schema import CountryCreate, CountryOut

router = APIRouter(prefix="/countries", tags=["Country"])

@router.post("/", response_model=CountryOut)
def create_country(country: CountryCreate, db: Session = Depends(get_db)):
    return country_service.create_country(db, country)

@router.get("/", response_model=list[CountryOut])
def list_countries(db: Session = Depends(get_db)):
    return country_service.get_all_countries(db)

@router.get("/{country_id}", response_model=CountryOut)
def get_country(country_id: int, db: Session = Depends(get_db)):
    result = country_service.get_country_by_id(db, country_id)
    if not result:
        raise HTTPException(status_code=404, detail="Country not found")
    return result

@router.delete("/{country_id}", response_model=CountryOut)
def delete_country(country_id: int, db: Session = Depends(get_db)):
    result = country_service.delete_country(db, country_id)
    if not result:
        raise HTTPException(status_code=404, detail="Country not found")
    return result