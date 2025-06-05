# PostgreSQL Migration Guide

This guide explains how to migrate the Consultigo application from SQLite to PostgreSQL.

## Changes Made

1. Updated `database.py` to use PostgreSQL instead of SQLite
2. Added PostgreSQL dependencies to `requirements.txt`
3. Set up Alembic for database migrations
4. Updated Docker Compose configuration to include PostgreSQL
5. Created scripts for database initialization and migrations

## Local Development Setup

1. Install PostgreSQL on your local machine
2. Create a `.env` file in the `backend` directory with the following content:
   ```
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/consultigo
   CORS_ORIGINS=http://localhost,http://frontend
   SECRET_KEY=your-secret-key-change-in-production
   ACCESS_TOKEN_EXPIRE_MINUTES=60
   ```
3. Initialize the database:
   ```bash
   cd backend
   python init_db.py
   ```
4. Run migrations:
   ```bash
   python run_migrations.py
   ```

## Docker Setup

1. Build and start the containers:
   ```bash
   docker-compose up -d
   ```
2. The database will be automatically initialized and migrations will be applied

## Data Migration

To migrate your existing SQLite data to PostgreSQL:

1. Export data from SQLite:
   ```bash
   sqlite3 consultigo.db .dump > data.sql
   ```
2. Convert the SQLite dump to PostgreSQL format (you may need to manually adjust some SQL syntax)
3. Import the data into PostgreSQL:
   ```bash
   psql -U postgres -d consultigo -f data.sql
   ```

## Deployment on Render

1. Create a PostgreSQL database on Render
2. Update the environment variables in your Render service:
   - `DATABASE_URL`: Your Render PostgreSQL connection string
   - `CORS_ORIGINS`: Your frontend URL
   - `SECRET_KEY`: A secure secret key
   - `ACCESS_TOKEN_EXPIRE_MINUTES`: 60 (or your preferred value)
3. Deploy your application

## Troubleshooting

### Connection Issues

- Ensure PostgreSQL is running and accessible
- Check that the connection string is correct
- Verify network connectivity between services

### Migration Issues

- If migrations fail, check the Alembic logs
- You may need to manually adjust migration scripts for PostgreSQL-specific features

### Data Migration Issues

- Some SQLite-specific features may not work in PostgreSQL
- You may need to manually adjust data types or constraints 