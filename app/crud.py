from app.models import Subscriber
from app.schemas import SubscriberCreate
from sqlalchemy.orm import Session


# Add new Subscriber to database
def create_new_subscriber(subscriber: SubscriberCreate, db: Session) -> Subscriber:
    new_subscriber = Subscriber(**subscriber.dict())
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


# Delete By Email
def delete_subscriber(email: str, db: Session) -> Subscriber:
    subscriber = get_subscriber_by_email(email, db)
    if not subscriber:
        return None

    db.delete(subscriber)
    db.commit()
    return subscriber
    