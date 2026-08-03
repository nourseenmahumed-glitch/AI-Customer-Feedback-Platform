from fastapi import FastAPI

from app.core.config import PROJECT_NAME, VERSION
from app.core.database import engine
from app.models.review import Review
from app.core.database import Base

app = FastAPI(
    title=PROJECT_NAME,
    version=VERSION
)

# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Backend is running successfully"
    }