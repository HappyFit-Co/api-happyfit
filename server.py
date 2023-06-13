from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from api import api
from api.utils.database import mongo

app = Flask(__name__)

CORS(app)

JWTManager(app)
app.config.from_object('config.Config')
mongo.init_app(app)

api.init_app(app) 



if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])