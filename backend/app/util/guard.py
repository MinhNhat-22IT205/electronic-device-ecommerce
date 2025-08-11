# from fastapi import Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# from app.db.db_session import get_db
# from app.util.jwt import decode_token
# from app.repository.user_repository import get_user_by_email
# from app.model.user import User
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
#
# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
#     payload = decode_token(token)
#     if not payload:
#         raise HTTPException(status_code=401, detail="Invalid token")
#
#     user = db.query(User).filter(User.id == int(payload["sub"])).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
