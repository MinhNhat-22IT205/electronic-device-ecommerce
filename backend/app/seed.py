from sqlalchemy.orm import Session
from backend.app.db.db_connect import SessionLocal, Base, engine
# from backend.app.model.user import User
from backend.app.model import Product, Color, ProductImage
from backend.app.util.security import hash_password
from datetime import datetime

# 1. Create tables if not exist
Base.metadata.create_all(bind=engine)

# 2. Start session
db: Session = SessionLocal()

# 3. Seed admin + customer if not exists
# def seed_users():
#     if not db.query(User).filter(User.email == "admin@example.com").first():
#         admin = User(
#             email="admin@example.com",
#             password=hash_password("admin123"),
#             role="admin",
#             first_name="Super",
#             last_name="Admin",
#             is_verified=True,
#             registered_at=datetime.utcnow()
#         )
#         db.add(admin)
#
#     if not db.query(User).filter(User.email == "customer@example.com").first():
#         customer = User(
#             email="customer@example.com",
#             password=hash_password("customer123"),
#             role="customer",
#             first_name="Minh",
#             last_name="Nhật",
#             is_verified=True,
#             registered_at=datetime.utcnow()
#         )
#         db.add(customer)
#
#     db.commit()
#     print("✅ Users seeded")

# 4. Seed sample products
def seed_products():
    if not db.query(Product).first():
        for i in range(1, 6):
            product = Product(
                name=f"Product {i}",
                sku=f"P{i:04}",
                description="Demo product",
                camera="12MP",
                cpu="Snapdragon",
                ram=8,
                rom=128,
                pin=5000,
                cost_price=100.0,
                sale_price=150.0,
                quantity=100,
                weight=0.5,
                width=7.0,
                height=15.0,
                thick=0.8,
                is_activated=True,
                is_deleted=False,
                created_at=datetime.utcnow()
            )
            db.add(product)

        db.commit()
        print("✅ Products seeded")

def seed_colors():
    color_names = ["Black", "White", "Blue", "Red", "Green"]
    for name in color_names:
        if not db.query(Color).filter(Color.name == name).first():
            db.add(Color(name=name))
    db.commit()
    print("✅ Colors seeded")

def seed_product_images():
    products = db.query(Product).all()
    colors = db.query(Color).all()

    for product in products:
        for i, color in enumerate(colors):
            image_path = f"images/{product.sku.lower()}_{color.name.lower()}.jpg"
            image = ProductImage(
                product_id=product.id,
                color_id=color.id,
                path=image_path,
                sort_order=i + 1
            )
            db.add(image)
    db.commit()
    print("✅ Product images seeded")

# Final seeding order
# seed_users()
seed_colors()
seed_products()
seed_product_images()
db.close()
