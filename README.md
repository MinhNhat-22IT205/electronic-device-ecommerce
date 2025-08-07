

# Ecommerce Backend Configuration

## 1. Setup

### Clone the Repository
```bash
git clone https://github.com/yourname/ecommerce-backend.git
cd ecommerce-backend
```

### Launch the Application
```bash
docker-compose up --build
```
This command initializes:
- FastAPI backend at `http://localhost:8000`
- Swagger API documentation at `http://localhost:8000/docs`
- MinIO storage at `http://localhost:9001`
- Nginx frontend at `http://localhost:80`

## 2. Alembic Database Migrations

### Create a New Migration
```bash
docker exec -it python-backend bash
alembic revision --autogenerate -m "Add description here"
```

### Apply Migrations
```bash
alembic upgrade head
```

## 3. Seeding Demo Data
```bash
docker exec -it python-backend python app/seed.py
```