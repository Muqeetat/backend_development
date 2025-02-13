FROM python:3.11

# Set working directory
WORKDIR /usr/src/app

# Copy dependencies file first (better caching)
COPY requirements.txt .

# install dependencies
RUN pip install --progress-bar off -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose FastAPI's default port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
