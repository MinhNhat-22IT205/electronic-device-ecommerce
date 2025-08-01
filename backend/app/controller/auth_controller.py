from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schema.user_schema import LoginRequest, TokenResponse, UserResponse, RegisterRequest
from app.db.db_session import get_db
from app.service.auth_service import authenticate_user, register_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    token, _ = authenticate_user(db, data.email, data.password)
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register", response_model=UserResponse)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    user = register_user(db, data)
    return user

