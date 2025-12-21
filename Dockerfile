FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./backend/

EXPOSE 8000

# Set Python path và chạy từ thư mục backend
WORKDIR /app/backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]