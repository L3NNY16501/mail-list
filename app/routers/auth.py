from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, security, crud
from app.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", response_model=schemas.Token)
def register(subscriber: schemas.SubscriberCreate, db: Session = Depends(get_db)):
    # Check if user exists
    existing_user = crud.get_subscriber_by_email(subscriber.email, db)
    if existing_user:
        raise HTTPException(status_code=404, detail="User already exists")
    
    # Create user in DB
    new_user = crud.create_new_subscriber(subscriber, db)
    
    # Return Token
    token = security.create_access_token({"sub": new_user.email})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=schemas.Token)
def login(subscriber: schemas.SubscriberLogin, db: Session = Depends(get_db)):
    db_subscriber = crud.get_subscriber_by_email(subscriber.email, db)
    if not db_subscriber:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    
    if crud.verify_subscriber_password(db_subscriber, subscriber) == False:
        raise HTTPException(status_code=404, detail="Incorrect Password")
    
    token = security.create_access_token({"sub": db_subscriber.email})
    return {"access_token": token, "token_type": "Bearer"}