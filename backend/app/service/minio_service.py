from minio import Minio
from app.config.env_config import env
from datetime import timedelta
from urllib.parse import urlparse
from minio.commonconfig import CopySource

minio_client = Minio(
    env.MINIO_ENDPOINT,
    access_key=env.MINIO_ACCESS_KEY,
    secret_key=env.MINIO_SECRET_KEY,
    secure=False  # True if using HTTPS
)

def ensure_bucket(bucket_name: str):
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)

def get_upload_url(bucket_name: str, object_name: str):
    
    ensure_bucket(bucket_name)

    url = minio_client.presigned_put_object(
        bucket_name,
        object_name,
        expires=timedelta(minutes=10) 
    )
    return url.replace("minio:9000", "localhost")

def get_presigned_url(bucket_name: str, object_name: str, expires_minutes=60):
    url = minio_client.presigned_get_object(
        bucket_name,
        object_name,
        expires=timedelta(minutes=expires_minutes)
    )
    return url.replace("minio:9000", "localhost")

def move_object(old_bucket: str, new_bucket:str, old_object_key: str, new_object_key: str):
    minio_client.copy_object(
        new_bucket,
        new_object_key,
        CopySource(old_bucket, old_object_key)
    )
    minio_client.remove_object(old_bucket, old_object_key)

def delete_object(bucket_name: str, object_name: str):
    try:
        minio_client.remove_object(bucket_name, object_name)
        print(f"🗑 Deleted {object_name} from {bucket_name}")
    except Exception as e:
        print(f"❌ Failed to delete {object_name}: {e}")
