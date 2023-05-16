from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restx import Resource

from api.controllers.exercises import ExerciseController
from api.schemas.exercises import ns, exercise_schema, unauthorized_schema, empty_list_schema, not_found_schema, unprocessable_schema

exercise_controller = ExerciseController()

@ns.route('/') 
class ExerciseList(Resource):
    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Retorna a lista de dados de exercício.')
    @ns.marshal_list_with(exercise_schema)
    @ns.response(200, 'Sucesso', [exercise_schema])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', empty_list_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    def get(self):
        """Lista todos os exercícios"""
        return exercise_controller.get_all_exercises()

@ns.route('/id/<string:exercise_id>')
class ExerciseById(Resource):
    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Retorna dados de um exercício pelo _id', params={'exercise_id': 'ID do exercício que deseja buscar'})
    @ns.response(200, 'Sucesso', exercise_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    @ns.expect({'exercise_id': str})
    def get(self, exercise_id):
        """Lista exercício pelo _id"""
        return exercise_controller.get_exercise_by_id(exercise_id)

@ns.route('/name/<string:exercise_name>')
class ExerciseByName(Resource):
    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Retorna dados de exercícios pelo nome', params={'exercise_name': 'Nome do exercício que deseja buscar'})
    @ns.marshal_list_with(exercise_schema, code=200)
    @ns.response(200, 'Sucesso', [exercise_schema])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', empty_list_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    @ns.expect({'exercise_name': str})
    def get(self, exercise_name):
        """Lista exercícios pelo name"""
        return exercise_controller.get_exercise_by_name(exercise_name)

@ns.route('/muscle/<string:exercise_target>')
class ExerciseByTarget(Resource):
    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Retorna lista de exercícios pelo músculo target', params={'exercise_target': 'Nome do músculo target que deseja buscar'})
    @ns.marshal_list_with(exercise_schema, code=200)
    @ns.response(200, 'Sucesso', [exercise_schema])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', empty_list_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    @ns.expect({'exercise_target': str})
    def get(self, exercise_target):
        """Lista exercícios pelo músculo target"""
        return exercise_controller.get_exercise_by_target(exercise_target)
