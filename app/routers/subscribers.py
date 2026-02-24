from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
import app.crud as crud, app.schemas as schemas


router = APIRouter()

# Create an endpoint for creating a new subscriber and storing in database
@router.post("/", response_model=schemas.SubscriberOut)
def create_new_subscriber(subscriber: schemas.SubscriberCreate, db: Session=Depends(get_db)) -> schemas.SubscriberOut:
    return crud.create_new_subscriber(subscriber, db)
    