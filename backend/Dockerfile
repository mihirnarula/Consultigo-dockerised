FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create migrations directory if it doesn't exist
RUN mkdir -p migrations/versions

# Expose the port the app runs on
EXPOSE 8000

# Create a startup script
RUN echo '#!/bin/bash\n\
echo "Waiting for PostgreSQL..."\n\
while ! pg_isready -h postgres -p 5432 -U postgres; do\n\
  sleep 1\n\
done\n\
echo "PostgreSQL is ready!"\n\
\n\
echo "Running database migrations..."\n\
python run_migrations.py\n\
\n\
echo "Starting the application..."\n\
uvicorn app.app:app --host 0.0.0.0 --port 8000\n\
' > /app/start.sh && chmod +x /app/start.sh

# Command to run the application
CMD ["/app/start.sh"] 