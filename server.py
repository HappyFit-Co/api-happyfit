from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from api import api
from api.utils.database import mongo

app = Flask(__name__)

# Configura o CORS
CORS(app, resources={r"/*": {"origins": "*"}},
     supports_credentials=True,
     allowed_headers=['Content-Type', 'Content-Length', 'Accept-Encoding', 'X-CSRF-Token', 'Authorization', 'accept', 'origin', 'Cache-Control', 'X-Requested-With'],
     methods=['POST', 'OPTIONS', 'GET', 'PUT', 'DELETE'])

JWTManager(app)
app.config.from_object('config.Config')
mongo.init_app(app)

# Configura a API com a instância do objeto api criada em api.__init__.py
api.init_app(app) 

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
