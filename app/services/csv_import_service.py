import pandas as pd
from datetime import datetime

from app.models.review import Review

def clean_float(value):
    """
    Convert rating values safely to float
    """

    if pd.isna(value):
        return None

    if isinstance(value, str):
        value = value.strip()

        if value == "":
            return None

    try:
        return float(value)

    except:
        return None



def import_reviews(file_path, db):

    df = pd.read_csv(file_path)

    print("Total rows:", len(df))

    imported = 0

    for index, row in df.iterrows():

        try:

            review = Review(

                branch=row.get("branch"),

                review_date=row.get("review_date"),

                original_review_text=row.get(
                    "original_review_text"
                ),

                normalized_review_text=row.get(
                    "normalized_review_text"
                ),

                sentiment_text=row.get(
                    "sentiment_text"
                ),

                topic_text=row.get(
                    "topic_text"
                ),


                # FIX FLOAT COLUMNS
                overall_rating=clean_float(
                    row.get("overall_rating")
                ),

                food_rating=clean_float(
                    row.get("food_rating")
                ),

                service_rating=clean_float(
                    row.get("service_rating")
                ),

                atmosphere_rating=clean_float(
                    row.get("atmosphere_rating")
                ),


                language_detected=row.get(
                    "language_detected"
                ),


                is_mixed_language=bool(
                    row.get("is_mixed_language")
                ),

                is_arabizi=bool(
                    row.get("is_arabizi")
                ),

                short_text_flag=bool(
                    row.get("short_text_flag")
                ),

                emoji_only_flag=bool(
                    row.get("emoji_only_flag")
                ),

                suspicious_text_flag=bool(
                    row.get("suspicious_text_flag")
                ),

                duplicate_flag=bool(
                    row.get("duplicate_flag")
                ),

                near_duplicate_flag=bool(
                    row.get("near_duplicate_flag")
                ),


                text_quality_score=row.get(
                    "text_quality_score"
                ),

                review_word_count=row.get(
                    "review_word_count"
                ),

                review_char_count=row.get(
                    "review_char_count"
                ),

                review_length_category=row.get(
                    "review_length_category"
                ),

                created_at=datetime.utcnow()

            )


            db.add(review)


            if imported % 1000 == 0:
                print(f"Imported {imported} rows...")


            imported += 1


        except Exception as e:

            print("\nError in row", index)

            print(row)

            raise e



    db.commit()

    print(
        f"Finished Importing {imported} rows"
    )

    return imported