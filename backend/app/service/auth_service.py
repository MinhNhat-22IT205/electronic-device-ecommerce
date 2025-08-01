from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repository.user_repository import get_user_by_email, create_user
from app.util.security import verify_password
from app.util.jwt import create_access_token
from app.schema.user_schema import RegisterRequest


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": str(user.id), "role": user.role})
    return access_token, user

def register_user(db: Session, data: RegisterRequest):
    if get_user_by_email(db, data.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = create_user(db, data)
    return user