import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import ProgrammingError

# Load environment variables
load_dotenv()

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Extract database name from URL
# Format: postgresql://username:password@host:port/dbname
db_name = DATABASE_URL.split("/")[-1]

# Create a connection to the default PostgreSQL database
# This is used to create our application database
default_db_url = DATABASE_URL.rsplit("/", 1)[0] + "/postgres"
engine = create_engine(default_db_url)

# Create the database if it doesn't exist
with engine.connect() as conn:
    try:
        conn.execute(text(f"CREATE DATABASE {db_name}"))
        print(f"Database '{db_name}' created successfully.")
    except ProgrammingError as e:
        if "already exists" in str(e):
            print(f"Database '{db_name}' already exists.")
        else:
            raise e

print("Database initialization complete.") 