# config.py
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = os.getenv("DEBUG")

if not DEBUG: #or not VARIABLE2:
    raise ValueError("Missing required environment variables")