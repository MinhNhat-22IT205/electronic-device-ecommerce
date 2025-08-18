from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.db.db_connect import Base, engine, SessionLocal
from app.model.user import User
from app.model.product import Product
from app.model.product_image import ProductImage
from app.util.security import hash_password
from app.util.hash import generate_object_key
from minio import Minio
from minio.error import S3Error
import os
from app.config.env_config import env

# Connect to MinIO (values from .env or docker-compose)
minio_client = Minio(
    env.MINIO_ENDPOINT,
    access_key=env.MINIO_ACCESS_KEY,
    secret_key=env.MINIO_SECRET_KEY,
    secure=False  # True if using HTTPS
)


# Create buckets if not exist
for bucket in [env.BUCKET_PRODUCT]:
    if not minio_client.bucket_exists(bucket):
        minio_client.make_bucket(bucket)
        print(f"✅ Bucket created: {bucket}")
    else:
        print(f"ℹ️ Bucket already exists: {bucket}")


# Create tables if they don't exist
Base.metadata.create_all(bind=engine)
db: Session = SessionLocal()

def seed_users():
    users = [
        {
            "email": "admin@example.com",
            "password": "admin123",
            "role": "admin",
            "first_name": "Super",
            "last_name": "Admin"
        },
        {
            "email": "user@example.com",
            "password": "string",
            "role": "customer",
            "first_name": "Minh",
            "last_name": "Nhật"
        }
    ]
    for u in users:
        if not db.query(User).filter(User.email == u["email"]).first():
            db.add(User(
                email=u["email"],
                password=hash_password(u["password"]),
                role=u["role"],
                first_name=u["first_name"],
                last_name=u["last_name"],
                is_verified=True,
                registered_at=datetime.utcnow()
            ))
    db.commit()
    print("✅ Users seeded")


def seed_products_with_images():
    # Absolute path to dummy images folder
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # where this seed file lives
    sample_dir = os.path.join(BASE_DIR, "data", "dummy_images") # Local folder with product images

    if not db.query(Product).first():
        for i in range(1, 30):
            product = Product(
                name=f"Product {i}",
                sku=f"P{i:04}",
                description="Demo product",
                camera="12MP",
                cpu="Snapdragon",
                ram=8,
                rom=128,
                pin=5000,
                cost_price=150.0,
                sale_price=100.0,
                quantity=100,
                weight=0.5,
                width=7.0,
                height=15.0,
                thick=0.8,
                is_activated=True,
                is_deleted=False,
            )
            db.add(product)
        db.commit()
        print("✅ Products seeded")

    # Upload images for each product
    products = db.query(Product).all()
    for product in products:
        for i in range(1, 3):  # Two sample images
            local_image_path = os.path.join(sample_dir, f"dummy{i}.jpg")
            if os.path.exists(local_image_path):
                object_path =  generate_object_key(f"p_image{i}.jpg")  # object inside bucket
                # Upload to MinIO
                minio_client.fput_object(env.BUCKET_PRODUCT, object_path, local_image_path)
                print(f"✅ Uploaded {object_path} to {env.BUCKET_PRODUCT}")

                # Save image path in DB (bucket/object)
                if not db.query(ProductImage).filter(ProductImage.path == f"{object_path}").first():
                    db.add(ProductImage(
                        product_id=product.id,
                        path=object_path
                    ))
    db.commit()
    print("✅ Product images seeded")

# Run seeds in order
seed_users()
seed_products_with_images()
db.close()
