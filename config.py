import os
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

    # Chave secreta para autenticação de sessão
    SECRET_KEY = os.environ.get('SECRET_KEY')
