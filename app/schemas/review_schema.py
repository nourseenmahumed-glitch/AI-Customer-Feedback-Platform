from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ReviewResponse(BaseModel):

    id: int

    branch: str

    review_date: Optional[str] = None

    original_review_text: Optional[str] = None

    normalized_review_text: Optional[str] = None

    sentiment_text: Optional[str] = None

    topic_text: Optional[str] = None

    overall_rating: Optional[float] = None

    food_rating: Optional[float] = None

    service_rating: Optional[float] = None

    atmosphere_rating: Optional[float] = None

    language_detected: Optional[str] = None

    is_mixed_language: Optional[bool] = None

    is_arabizi: Optional[bool] = None

    short_text_flag: Optional[bool] = None

    emoji_only_flag: Optional[bool] = None

    suspicious_text_flag: Optional[bool] = None

    duplicate_flag: Optional[bool] = None

    near_duplicate_flag: Optional[bool] = None

    text_quality_score: Optional[float] = None

    review_word_count: Optional[int] = None

    review_char_count: Optional[int] = None

    review_length_category: Optional[str] = None

    created_at: Optional[datetime] = None


    class Config:
        from_attributes = True