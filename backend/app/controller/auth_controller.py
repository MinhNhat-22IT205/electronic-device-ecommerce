# from fastapi import APIRouter, Depends, Response, Request, HTTPException
# from sqlalchemy.orm import Session
# from backend.app.util.jwt import create_access_token, create_refresh_token, decode_token
# from backend.app.schema.user_schema import LoginRequest, TokenResponse, UserResponse, RegisterRequest
# from backend.app.db.db_session import get_db
# from backend.app.service.auth_service import authenticate_user, register_user, validate_and_decode_refresh_token
#
# router = APIRouter(prefix="/auth", tags=["Auth"])
#
# @router.post("/login", response_model=TokenResponse)
# def login(data: LoginRequest, db: Session = Depends(get_db), response: Response = None):
#     access_token, refresh_token, _ = authenticate_user(db, data.email, data.password)
#
#     # Set refresh token in HttpOnly cookie
#     response.set_cookie(
#         key="refresh_token",
#         value=refresh_token,
#         httponly=True,
#         samesite="strict",
#         secure=False
#     )
#
#     return {"access_token": access_token, "token_type": "bearer"}
#
# @router.post("/register", response_model=UserResponse)
# def register(data: RegisterRequest, db: Session = Depends(get_db)):
#     user = register_user(db, data)
#     return user
#
# @router.post("/refresh", response_model=TokenResponse)
# def refresh_token (request: Request, db: Session = Depends(get_db), response: Response = None):
#     refresh_token = request.cookies.get("refresh_token")
#     if not refresh_token:
#         raise HTTPException(status_code=401, detail="No refresh token")
#
#     user = validate_and_decode_refresh_token(db, refresh_token)
#
#     new_access_token = create_access_token({"sub": str(user.id), "role": user.role})
#
#     new_refresh_token = create_refresh_token({"sub": str(user.id)})
#
#     response.set_cookie(
#         key="refresh_token",
#         value=new_refresh_token,
#         httponly=True,
#         samesite="strict",
#         secure=False
#     )
#
#     return {"access_token": new_access_token, "token_type": "bearer"}
#
