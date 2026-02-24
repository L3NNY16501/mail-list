from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

# Load environment Variables
load_dotenv()

# Create Database URL
DB_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASS')}@"
    f"{os.getenv('DB_HOST')}/"
    f"{os.getenv('DB_NAME')}"
)

# Configure engine 
engine = create_engine(DB_URL, echo=True)

# Create Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()