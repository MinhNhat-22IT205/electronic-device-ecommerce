from backend.app.config.db_connect import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()