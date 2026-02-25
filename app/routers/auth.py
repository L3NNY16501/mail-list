from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, security, crud
from app.database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", response_model=schemas.SubscriberOut)
def register(subscriber: schemas.SubscriberCreate, db: Session = Depends(get_db)):
    # Check if user exists
    existing_user = crud.get_subscriber_by_email(subscriber.email, db)
    if existing_user:
        raise HTTPException(status_code=404, detail="User already exists")
    
    # Create user in DB
    new_user = crud.create_new_subscriber(subscriber, db)
    
    # Return Token
    return new_user


@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
    ):
    
    email = form_data.username
    password=form_data.password
    
    db_subscriber = crud.get_subscriber_by_email(email, db)
    if not db_subscriber:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    
    if crud.verify_subscriber_password(password, db_subscriber) == False:
        raise HTTPException(status_code=404, detail="Incorrect Password")
    
    # Return Token
    token = security.create_access_token({"sub": db_subscriber.email})
    return {"access_token": token, "token_type": "Bearer"}