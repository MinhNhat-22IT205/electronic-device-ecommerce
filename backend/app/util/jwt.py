# from datetime import datetime, timedelta
# from jose import jwt, JWTError
# from typing import Optional
# from app.config.env_config import env
#
# ACCESS_TOKEN_EXPIRE_MINUTES = 60
# REFRESH_TOKEN_EXPIRE_DAYS = 7
#
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, env.JWT_SECRET_KEY, algorithm=env.JWT_ALGORITHM)
#
# def create_refresh_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, env.JWT_SECRET_KEY, algorithm=env.JWT_ALGORITHM)
#
# def decode_token(token: str):
#     try:
#         payload = jwt.decode(token, env.JWT_SECRET_KEY, algorithms=[env.JWT_ALGORITHM])
#         return payload
#     except JWTError:
#         return None
