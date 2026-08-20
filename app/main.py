from fastapi import FastAPI

from app.core.config import PROJECT_NAME, VERSION
from app.core.database import engine, Base
from app.api.review_routes import router as review_router

from app.models.review import Review

app = FastAPI(
    title=PROJECT_NAME,
    version=VERSION
)

# Register API routes
app.include_router(review_router)

# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Backend is running successfully"
    }