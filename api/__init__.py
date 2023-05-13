from flask_restx import Api
from flask_pymongo import PyMongo

# Inicializa a extensão PyMongo
mongo = PyMongo()

# Cria o objeto Api, que é uma extensão do Flask
api = Api(version='1.0', title='API RESTful - HappyFit', description='Uma simples API construída com Flask-RESTX')

# Importa os namespaces criados
from api.routes.exercises import ns as exercise_namespace

# Adiciona os namespaces à API
api.add_namespace(exercise_namespace)

