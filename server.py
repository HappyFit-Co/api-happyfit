from flask import Flask
from flask_restx import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

# Importando a API
from api.routes.users import api as user_api

class Server():
    app = Flask(__name__)
    api = Api(app, version='v1', title='Awesome Project')

    # Registrando recursos da API
    api.add_namespace(user_api)

    # Configurando documentação
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='Awesome Project',
            version='v1',
            plugins=[MarshmallowPlugin()],
            openapi_version='3.0.0'
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',  # URI para acessar a documentação da API em JSON
        'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI para acessar a UI da documentação da API
    })

    docs = FlaskApiSpec(app)
    docs.register(user_api)

if __name__ == '__main__':
    server = Server()
    server.app.run(debug=True)
