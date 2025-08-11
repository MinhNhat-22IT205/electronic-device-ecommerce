# from sqlalchemy.orm import Session
# from backend.app.model.user import User
# from backend.app.schema.user_schema import RegisterRequest
# from backend.app.util.security import hash_password
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()
#
# def create_user(db: Session, user: RegisterRequest):
#     new_user = User(
#         email=user.email,
#         password=hash_password(user.password),
#         first_name=user.first_name,
#         last_name=user.last_name,
#         role="customer"
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
# def get_user_by_id(db: Session, id:str):
#     return db.get(User, id)