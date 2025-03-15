# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the application files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir flask pytesseract pillow

# Expose the Flask application port
EXPOSE 5001

# Run the Flask app when the container starts
CMD ["python", "app.py"]
