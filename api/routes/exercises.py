from flask import abort
from flask_restx import Resource
from api.controllers.exerciseController import ExerciseController
from api.schemas.exerciseSchema import ns, exercise_schema

exercise_controller = ExerciseController()

@ns.route('/')
class ExerciseList(Resource):
    @ns.marshal_list_with(exercise_schema)
    @ns.expect({})
    def get(self):
        """
        Retorna a lista de dados de exercício
        """
        exercises = exercise_controller.get_all_exercises()
        if not exercises:
            return {'message': 'No exercises found'}, 404
        return exercises

@ns.route('/id/<string:exercise_id>')
class ExerciseById(Resource):
    @ns.marshal_with(exercise_schema)
    @ns.expect({'exercise_id': str})
    def get(self, exercise_id):
        """
        Retorna dados de um exercício pelo _id
        """
        exercises = exercise_controller.get_exercise_by_id(exercise_id)
        if not exercises:
            return {'message': 'No exercise found'}, 404
        return exercises

@ns.route('/name/<string:exercise_name>')
class ExerciseByName(Resource):
    @ns.marshal_with(exercise_schema)
    @ns.expect({'exercise_name': str})
    def get(self, exercise_name):
        """
        Retorna dados de um exercício pelo nome
        """
        exercises = exercise_controller.get_exercise_by_name(exercise_name)
        if not exercises:
            return {'message': 'No exercises found'}, 404
        return exercises

@ns.route('/muscle/<string:exercise_target>')
class ExerciseByTarget(Resource):
    @ns.marshal_list_with(exercise_schema)
    @ns.expect({'exercise_target': str})
    def get(self, exercise_target):
        """
        Retorna lista de exercícios pelo músculo target
        """
        exercises = exercise_controller.get_exercise_by_target(exercise_target)
        if not exercises:
            return {'message': 'No exercises found'}, 404
        return exercises
