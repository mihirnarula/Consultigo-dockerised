import os
import subprocess
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def wait_for_postgres():
    """Wait for PostgreSQL to be ready"""
    print("Waiting for PostgreSQL to be ready...")
    max_retries = 30
    retry_interval = 2
    
    for i in range(max_retries):
        try:
            # Try to run a simple command to check if PostgreSQL is ready
            subprocess.run(
                ["psql", os.getenv("DATABASE_URL"), "-c", "SELECT 1"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print("PostgreSQL is ready!")
            return True
        except subprocess.CalledProcessError:
            print(f"PostgreSQL is not ready yet. Retrying in {retry_interval} seconds... ({i+1}/{max_retries})")
            time.sleep(retry_interval)
    
    print("Failed to connect to PostgreSQL after maximum retries.")
    return False

def run_migrations():
    """Run database migrations"""
    if not wait_for_postgres():
        return False
    
    print("Running database migrations...")
    
    # Initialize Alembic if not already initialized
    if not os.path.exists("migrations/versions"):
        print("Initializing Alembic...")
        subprocess.run(["alembic", "init", "migrations"], check=True)
    
    # Create initial migration
    print("Creating initial migration...")
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", "Initial migration"], check=True)
    
    # Apply migrations
    print("Applying migrations...")
    subprocess.run(["alembic", "upgrade", "head"], check=True)
    
    print("Migrations completed successfully!")
    return True

if __name__ == "__main__":
    run_migrations() 