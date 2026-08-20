from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.csv_import_service import import_reviews

from app.models.review import Review
from app.schemas.review_schema import ReviewResponse


router = APIRouter()


@router.post("/import-csv")
def import_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    import_reviews(file_path, db)

    return {
        "message": "Import Finished Successfully"
    }


@router.get("/reviews/", response_model=list[ReviewResponse])
def get_reviews(
    db: Session = Depends(get_db)
):
    reviews = db.query(Review).limit(10).all()

    return reviews


@router.get("/dashboard/summary")
def get_dashboard_summary(
    db: Session = Depends(get_db)
):
    total_reviews = db.query(Review).count()

    positive_reviews = db.query(Review).filter(
        Review.sentiment_text.ilike("%positive%")
    ).count()

    negative_reviews = db.query(Review).filter(
        Review.sentiment_text.ilike("%negative%")
    ).count()

    neutral_reviews = db.query(Review).filter(
        Review.sentiment_text.ilike("%neutral%")
    ).count()

    return {
        "total_reviews": total_reviews,
        "positive_reviews": positive_reviews,
        "negative_reviews": negative_reviews,
        "neutral_reviews": neutral_reviews
    }