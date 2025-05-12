# Docker Setup for Consultigo

This document explains how to run the Consultigo application using Docker.

## Prerequisites

- Docker and Docker Compose installed on your system
- Git (to clone the repository)

## Quick Start

1. Clone the repository (if you haven't already):
   ```bash
   git clone https://github.com/yourusername/consultigo-home.git
   cd consultigo-home
   ```

2. Build and start the containers:
   ```bash
   docker-compose up -d
   ```

3. Access the application:
   - Frontend: http://localhost
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Configuration

### Environment Variables

The backend service uses the following environment variables that you can modify in the `docker-compose.yaml` file:

- `DATABASE_URL`: SQLite database connection string
- `CORS_ORIGINS`: Allowed origins for CORS
- `SECRET_KEY`: Secret key for JWT token generation
- `ACCESS_TOKEN_EXPIRE_MINUTES`: JWT token expiration time

### Volumes

- The SQLite database file is mounted as a volume to persist data between container restarts

## Development Workflow

1. Make changes to your code locally
2. Rebuild the containers:
   ```bash
   docker-compose up -d --build
   ```

## Troubleshooting

### Backend Container Not Starting

Check the logs for any errors:
```bash
docker-compose logs backend
```

### Database Issues

If you encounter database issues, you might need to run the database setup script:
```bash
docker-compose exec backend python run_setup.py
```

### Frontend Not Connecting to Backend

Make sure the Nginx configuration is correctly set up to proxy API requests to the backend. 