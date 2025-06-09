# Use the official Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port on which the application will run
EXPOSE 8000

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "api:app", "--host", "127.0.0.1", "--port", "8000"]