from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME")
VERSION = os.getenv("VERSION")
DATABASE_URL = os.getenv("DATABASE_URL")