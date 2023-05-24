from flask_jwt_extended import jwt_required
from flask_restx import Resource

from api.controllers.exercises import ExerciseController
from api.schemas.exercises import ns, exercise_schema
from api.schemas.responses import (
    unauthorized_schema,
    empty_list_schema,
    not_found_schema,
    unprocessable_schema,
    internal_server_schema
)

@ns.route('/') 
class ExerciseList(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna a lista de dados de exercício')
    @ns.response(200, 'Sucesso', [exercise_schema])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', empty_list_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self):
        """Lista todos os exercícios"""
        return ExerciseController.get_all_exercises()

@ns.route('/id/<string:exercise_id>')
class ExerciseById(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna dados de um exercício pelo _id')
    @ns.param('exercise_id', 'ID do exercício que deseja buscar', _in='query', required=True, type='string')
    @ns.response(200, 'Sucesso', exercise_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self, exercise_id):
        """Lista exercício pelo _id"""
        return ExerciseController.get_exercise_by_id(exercise_id)

@ns.route('/name/<string:exercise_name>')
class ExerciseByName(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna dados de exercícios pelo nome')
    @ns.param('exercise_name', 'Nome do exercício que deseja buscar', _in='query', required=True, type='string')
    @ns.response(200, 'Sucesso', [exercise_schema])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', empty_list_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self, exercise_name):
        """Lista exercícios pelo name"""
        return ExerciseController.get_exercise_by_name(exercise_name)

@ns.route('/muscle/<string:exercise_target>')
class ExerciseByTarget(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna lista de exercícios pelo músculo target')
    @ns.param('exercise_target', 'Nome do músculo target que deseja buscar', _in='query', required=True, type='string')
    @ns.response(200, 'Sucesso', [exercise_schema])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', empty_list_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self, exercise_target):
        """Lista exercícios pelo músculo target"""
        return ExerciseController.get_exercise_by_target(exercise_target)
