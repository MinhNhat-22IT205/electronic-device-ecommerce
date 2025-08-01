# Sử dụng Python 3.10 làm base image
FROM python:3.10-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy các file requirements vào container
COPY requirements.txt .

# Cài đặt dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn app vào container
COPY . .

ENV PYTHONPATH=/app

# Expose cổng server (ví dụ 8000 cho FastAPI)
EXPOSE 8000

# Lệnh khởi chạy server (ví dụ FastAPI dùng uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]