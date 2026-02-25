from pydantic import EmailStr, BaseModel
from datetime import datetime


# Create Schema for subscriber creation
class SubscriberCreate(BaseModel):
    email: EmailStr
    password: str
    
# User Login Schema
class SubscriberLogin(BaseModel):
    email: EmailStr
    password: str
    
# Token response
class Token(BaseModel):
    access_token: str
    token_type: str
    
# Create Schema for returning subscriber information
class SubscriberOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class config:
        orm_mode = True