from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
import app.crud as crud, app.schemas as schemas
from app.security import get_current_user, verify_token


router = APIRouter(
    prefix=("/subscribers"),
    tags=["Subscribers"]
)

# Create a protected endpoint for logged in and authenticated Users
@router.get("/user-info", response_model=schemas.SubscriberOut)
def get_user_information(current_user_email = Depends(get_current_user), db: Session = Depends(get_db)):
    return crud.get_subscriber_by_email(current_user_email, db)

# Endpoint for Returning all emails in database
@router.get("/emails", response_model = list[schemas.SubscriberOut])
def get_all_email(db: Session=Depends(get_db)):
    return crud.get_all_emails(db)

# Endpoint for Deleting an Email from the database
@router.delete("/unsubscribe", response_model = schemas.SubscriberOut)
def unsubscribe(email: str, db: Session = Depends(get_db)):
    db_subscriber = crud.get_subscriber_by_email(email, db)
    if not db_subscriber:
        raise HTTPException(status_code=404, detail="Email not found")
    return crud.delete_subscriber(db_subscriber, db)
    