import os
from dotenv import load_dotenv
from datetime import timedelta


#loads environment variables from .env file


load_dotenv()
print(os.getenv('DATABASE_URL'))

class Config:
    #database
    SQLALCHEMY_DATABASE_URI =os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    #Security
    SECRET_KEY=os.getenv('SECRET_KEY')
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=24)

    #claude
    ANTHROPIC_API_KEY=os.getenv('ANTHROPIC_API_KEY')

