import os
from dotenv import load_dotenv

"""Set Flask configuration vars from .env file."""

load_dotenv()  # Load environment variables from .env file


class Config:
    """Set Flask configuration vars from .env file."""

    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://staycation:Clever-Forest-Pathway-92-Jump-Kite@51.8.81.142:3306/staycation')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

