from flask import abort
from flask_restx import Resource, fields
from api.controllers.exerciseController import ExerciseController
from api.schemas.exerciseSchema import ns, exercise_schema

exercise_controller = ExerciseController()

@ns.route('/')
class ExerciseList(Resource):
    @ns.doc(description='Retorna a lista de dados de exercício')
    @ns.marshal_list_with(exercise_schema)
    @ns.expect({})
    def get(self):
        """Lista todos os exercícios"""
        return exercise_controller.get_all_exercises()

@ns.route('/id/<string:exercise_id>')
class ExerciseById(Resource):
    @ns.doc(params={'exercise_id': 'ID do exercício que deseja buscar'})
    @ns.marshal_with(exercise_schema)
    @ns.expect({'exercise_id': str})
    def get(self, exercise_id):
        """
        Retorna dados de um exercício pelo _id
        """
        exercises = exercise_controller.get_exercise_by_id(exercise_id)
        if exercises is None or not exercises:
            return {'message': 'No exercise found'}, 404
        return exercises

@ns.route('/name/<string:exercise_name>')
class ExerciseByName(Resource):
    @ns.marshal_with(exercise_schema)
    #@ns.response(404, {'message': 'No exercises found'})
    @ns.param('exercise_name', 'Nome do exercício', _in='query', required=True, type=str)
    @ns.expect({'exercise_name': str})
    def get(self, exercise_name):
        """
        Retorna dados de um exercício pelo nome
        """
        return exercise_controller.get_exercise_by_name(exercise_name)

@ns.route('/muscle/<string:exercise_target>')
class ExerciseByTarget(Resource):
    @ns.marshal_list_with(exercise_schema)
    @ns.expect({'exercise_target': str})
    def get(self, exercise_target):
        """
        Retorna lista de exercícios pelo músculo target
        """
        exercises = exercise_controller.get_exercise_by_target(exercise_target)
        if exercises is None or not exercises:
            return {'message': 'No exercises found'}, 404
        return exercises
