from pydantic_settings import BaseSettings

class Config(BaseSettings):
    # Database
    DATABASE_URL: str
    MYSQL_ROOT_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str 

    # MinIO
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

env = Config()