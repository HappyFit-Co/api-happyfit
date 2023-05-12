from flask import Flask
from flask_restx import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

# Resources
from api.routes.users import Users
# Database
from api.utils.database import init_db

class Server():
    host: str = None
    port: str = 8080
    debug: bool = True

    app = None
    api = None

    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.api = Api(self.app, version='v1', title='Awesome Project')

        # Database config
        self.app.config['MONGO_URI'] = 'mongodb+srv://vinicin:i0W7rFpzsPPHtQXl@fitdb.orqhkym.mongodb.net/'
        init_db(self.app)

        # Import config
        self.app.config.from_pyfile('config.py')

        # Registrando resources
        self.api.add_resource(Users, '/users', endpoint='users')
        self.api.add_resource(Users, '/users/<string:user_id>', endpoint='user')

        # Configurando documentação
        self.app.config.update({
            'APISPEC_SPEC': APISpec(
                title='Awesome Project',
                version='v1',
                plugins=[MarshmallowPlugin()],
                openapi_version='3.0.0'
            ),
            'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
            'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
        })

        self.docs = FlaskApiSpec(self.app)
        self.docs.register(Users)

server = Server()

if __name__ == '__main__':
    app = server.app
    app.run(host=server.host, port=server.port, debug=server.debug)
