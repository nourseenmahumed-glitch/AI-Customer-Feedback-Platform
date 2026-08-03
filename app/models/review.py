from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime

from app.core.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    place_name = Column(String, nullable=False)

    reviewer_name = Column(String, nullable=False)

    rating = Column(Float, nullable=False)

    review_text = Column(Text, nullable=False)

    review_date = Column(String)

    sentiment = Column(String, default="Unknown")

    category = Column(String, default="General")

    created_at = Column(DateTime, default=datetime.utcnow)