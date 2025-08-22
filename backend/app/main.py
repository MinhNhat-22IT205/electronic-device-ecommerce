from fastapi import FastAPI
from app.db.db_connect import Base, engine
from app.controller import auth_controller, product_controller, cart_controller  #  import routers
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Register routers
app.include_router(auth_controller.router, prefix="/api")
app.include_router(product_controller.router, prefix="/api")
app.include_router(cart_controller.router, prefix="/api")
