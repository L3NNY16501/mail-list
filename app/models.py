from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func


Base = declarative_base()


class Subscriber(Base):
    __tablename__ = "subscribers"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
