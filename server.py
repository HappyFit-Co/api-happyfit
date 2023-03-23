from flasgger import Swagger
from flask import Flask
from flask_pymongo import PyMongo

# Blueprints
from api.routes.consumptions import consumptions_bp
from api.routes.diets import diets_bp
from api.routes.exercises import exercises_bp
from api.routes.historics import historics_bp
from api.routes.users import users_bp
# Database
from api.utils.database import init_db


class Server():
    host: str = None
    port: str = "8080"
    debug: bool = True

    app = None
    swagger = None

    def __init__(self) -> None:
        self.app = Flask(__name__)

        self.app.config['MONGO_URI'] = 'mongodb+srv://admin:UJBfUiR5KEFylFUt@fitdb.orqhkym.mongodb.net/test'

        init_db(self.app)

        self.app.config['SWAGGER'] = {
            'title': 'API Flask - HappyFit',
        }
        self.swagger = Swagger(self.app)

        self.app.config.from_pyfile('config.py')

        # Registrando blueprints
        self.app.register_blueprint(users_bp, url_prefix='/users')
        self.app.register_blueprint(historics_bp, url_prefix='/historics')
        self.app.register_blueprint(exercises_bp, url_prefix='/exercises')
        self.app.register_blueprint(diets_bp, url_prefix='/diets')
        self.app.register_blueprint(consumptions_bp, url_prefix='/consumptions')



server = Server()

if __name__ == '__main__':

    app = server.app

    app.run(host=server.host, port=server.port, debug=server.debug)
