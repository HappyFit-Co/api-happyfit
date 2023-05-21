from flask_jwt_extended import jwt_required
from flask_restx import Resource

from api.controllers.foods import FoodController
from api.schemas.foods import ns, food_schema
from api.schemas.response import (
    unauthorized_schema,
    empty_list_schema,
    not_found_schema,
    unprocessable_schema,
    internal_server_schema
)

@ns.route('/') 
class FoodList(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna a lista de dados de alimentos')
    @ns.response(200, 'Sucesso', [food_schema])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', empty_list_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self):
        """Lista todos os alimentos"""
        return FoodController.get_all_foods()

@ns.route('/id/<string:food_id>')
class FoodById(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna dados de um alimento pelo _id')
    @ns.param('food_id', 'ID do alimento que deseja buscar', _in='query', required=True, type='string')
    @ns.response(200, 'Sucesso', food_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self, food_id):
        """Lista alimento pelo _id"""
        return FoodController.get_food_by_id(food_id)

@ns.route('/name/<string:food_name>')
class FoodByName(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna dados de alimentos pelo nome', params={'food_name': 'Nome do alimento que deseja buscar'})  
    @ns.param('food_name', 'Nome do alimento que deseja buscar', _in='query', required=True, type='string')
    @ns.response(200, 'Sucesso', [food_schema])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', empty_list_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self, food_name):
        """Lista alimentos pelo name"""
        return FoodController.get_food_by_name(food_name)