from app.models import Subscriber
from app.schemas import SubscriberCreate, SubscriberOut, SubscriberLogin
from sqlalchemy.orm import Session
from app import security


# Add new Subscriber to database
def create_new_subscriber(subscriber: SubscriberCreate, db: Session) -> Subscriber:
    hashed = security.hash_password(subscriber.password)
    new_subscriber = Subscriber(
        email=subscriber.email,
        hashed_password=hashed
    )
    db.add(new_subscriber)
    db.commit()
    db.refresh(new_subscriber)
    return new_subscriber


# Get Subcriber by email
def get_subscriber_by_email(email: str, db: Session) -> Subscriber:
    subscriber = db.query(Subscriber).filter(Subscriber.email == email).first()
    if not subscriber:
        return None
    return subscriber

# Verifies Hashed password
def verify_subscriber_password(password_input: str , db_subscriber: Subscriber) -> bool:
    return security.verify_password(password_input, db_subscriber.hashed_password)
        
    
  
# Get all emails in database - Returns a list of Subscriber objects (records in table)
def get_all_emails(db: Session) -> list[SubscriberOut]:
    return db.query(Subscriber).all()


# Delete By Email
def delete_subscriber(subscriber: Subscriber, db: Session) -> Subscriber:
    db.delete(subscriber)
    db.commit()
    return subscriber
    