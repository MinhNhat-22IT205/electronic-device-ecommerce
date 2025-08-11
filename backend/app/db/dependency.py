from backend.app.config.database import SessionLocal

def get_db():
    mysql = SessionLocal()
    try:
        yield mysql
    finally:
        mysql.close()
