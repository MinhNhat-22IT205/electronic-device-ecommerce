from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.dependency import get_db
from backend.app.service import city_service
from backend.app.schema.city_schema import CityCreate, CityOut

router = APIRouter(prefix="/cities", tags=["City"])

@router.post("/", response_model=CityOut)
def create_city(city: CityCreate, db: Session = Depends(get_db)):
    return city_service.create_city(db, city)

@router.get("/", response_model=list[CityOut])
def list_cities(db: Session = Depends(get_db)):
    return city_service.get_all_cities(db)

@router.get("/{city_id}", response_model=CityOut)
def get_city(city_id: int, db: Session = Depends(get_db)):
    result = city_service.get_city_by_id(db, city_id)
    if not result:
        raise HTTPException(status_code=404, detail="City not found")
    return result

@router.delete("/{city_id}", response_model=CityOut)
def delete_city(city_id: int, db: Session = Depends(get_db)):
    result = city_service.delete_city(db, city_id)
    if not result:
        raise HTTPException(status_code=404, detail="City not found")
    return result