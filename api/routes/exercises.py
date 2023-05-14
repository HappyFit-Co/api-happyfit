from flask_restx import Resource
from api.controllers.exerciseController import ExerciseController
from api.schemas.exerciseSchema import ns, exercise_schema

exercise_controller = ExerciseController()

@ns.route('/')
class ExerciseList(Resource):
    @ns.marshal_list_with(exercise_schema)
    def get(self):
        """
        Retorna a lista de dados de exercício
        """
        return exercise_controller.get_all_exercises()

    @ns.expect(exercise_schema)
    @ns.marshal_with(exercise_schema, code=201)
    def post(self):
        """
        Adiciona um novo dado à lista de exercício
        """
        new_exercise = ns.payload
        return exercise_controller.add_new_exercise(new_exercise)
