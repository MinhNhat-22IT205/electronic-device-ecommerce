# from sqlalchemy.orm import Session
# from fastapi import HTTPException
# from backend.app.repository.user_repository import get_user_by_email, create_user, get_user_by_id
# from backend.app.util.security import verify_password
# from backend.app.util.jwt import create_access_token, create_refresh_token, decode_token
# from backend.app.schema.user_schema import RegisterRequest
#
#
# def authenticate_user(db: Session, email: str, password: str):
#     user = get_user_by_email(db, email)
#     if not user or not verify_password(password, user.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#
#     access_token = create_access_token(data={"sub": str(user.id), "role": user.role})
#
#     refresh_token = create_refresh_token({"sub": str(user.id)})
#
#     return access_token, refresh_token, user
#
# def register_user(db: Session, data: RegisterRequest):
#     if get_user_by_email(db, data.email):
#         raise HTTPException(status_code=400, detail="Email already registered")
#     user = create_user(db, data)
#     return user
#
# def validate_and_decode_refresh_token(db:Session, refresh_token: str):
#     payload = decode_token(refresh_token)
#     if not payload:
#         raise HTTPException(status_code=401, detail="Invalid or expired refresh token")
#
#     user_id = int(payload["sub"])
#     user = get_user_by_id(db, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
#