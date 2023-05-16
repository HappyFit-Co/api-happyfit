import os
from datetime import timedelta

from dotenv import load_dotenv

# carrega as configurações do arquivo .env
load_dotenv()

class Config:
    # Configurações do MongoDB
    MONGO_URI = os.environ.get('MONGO_URI')

    # Configurações do Flask
    DEBUG = os.environ.get('DEBUG', True)
    HOST = os.environ.get('HOST', 'localhost')
    PORT = os.environ.get('PORT', 5000)

    # Configurações do Flask-RESTX
    RESTX_MASK_SWAGGER = os.environ.get('RESTX_MASK_SWAGGER', False)
   
    # Configurações do JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 6))
    )
