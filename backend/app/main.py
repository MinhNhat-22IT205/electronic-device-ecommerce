from fastapi import FastAPI
from backend.app.controller import product_controller,bank_controller, admin_role_controller, role_controller, country_controller, \
    customer_controller, cart_controller, cart_item_controller, city_controller, category_controller, \
    customer_bank_controller, contact_controller, customer_role_controller, orders_controller, order_detail_controller, \
    product_category_controller, product_image_controller, product_review_controler, wishlist_controller, \
    admin_controller,  auth_controller
from backend.app.db.db_connect import Base, engine

from backend.app.model import *

Base.metadata.create_all(bind=engine)
app = FastAPI()

#  Register routers

app.include_router(auth_controller.router)
app.include_router(role_controller.router)
app.include_router(admin_role_controller.router)
app.include_router(bank_controller.router)
app.include_router(country_controller.router)
app.include_router(customer_controller.router)
app.include_router(cart_controller.router)
app.include_router(product_controller.router)
app.include_router(cart_item_controller.router)
app.include_router(category_controller.router)
app.include_router(city_controller.router)
app.include_router(contact_controller.router)
app.include_router(customer_bank_controller.router)
app.include_router(customer_role_controller.router)
app.include_router(orders_controller.router)
app.include_router(order_detail_controller.router)
app.include_router(product_category_controller.router)
app.include_router(product_image_controller.router)
app.include_router(product_review_controler.router)
app.include_router(wishlist_controller.router)
app.include_router(admin_controller.router)
