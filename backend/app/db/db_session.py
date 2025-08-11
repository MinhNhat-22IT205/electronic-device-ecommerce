from backend.app.db.db_connect import SessionLocal

def get_db():
    mysql = SessionLocal()
    try:
        yield mysql
    finally:
        mysql.close()