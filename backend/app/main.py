from fastapi import FastAPI
from app.db.db_connect import Base, engine
from app.controller import auth_controller, product_controller  #  import routers

Base.metadata.create_all(bind=engine)

app = FastAPI()

#  Register routers
app.include_router(auth_controller.router)
app.include_router(product_controller.router)
