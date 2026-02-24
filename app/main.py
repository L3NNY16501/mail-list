from fastapi import FastAPI
from app.routers import subscribers
import app.models as models
from app.database import engine


app = FastAPI(title="Skedaddle Mail List")
app.include_router(subscribers.router)


models.Base.metadata.create_all(bind=engine)

