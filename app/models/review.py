from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Text,
    DateTime
)
from datetime import datetime

from app.core.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    branch = Column(String, nullable=False)

    review_date = Column(String)

    original_review_text = Column(Text)

    normalized_review_text = Column(Text)

    sentiment_text = Column(String)

    topic_text = Column(String)

    overall_rating = Column(Float)

    food_rating = Column(Float)

    service_rating = Column(Float)

    atmosphere_rating = Column(Float)

    language_detected = Column(String)

    is_mixed_language = Column(Boolean)

    is_arabizi = Column(Boolean)

    short_text_flag = Column(Boolean)

    emoji_only_flag = Column(Boolean)

    suspicious_text_flag = Column(Boolean)

    duplicate_flag = Column(Boolean)

    near_duplicate_flag = Column(Boolean)

    text_quality_score = Column(Float)

    review_word_count = Column(Integer)

    review_char_count = Column(Integer)

    review_length_category = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)