from flask_restx import Namespace, Resource, fields
from flask import request
from api.utils.database import mongo
# from api import api
from api.schemas.exerciseSchema import ns, exercise_schema

@ns.route('/')
class ExerciseList(Resource):
    @ns.marshal_list_with(exercise_schema)
    def get(self):
        """
        Retorna a lista de dados de exercício
        """
        exercises = list(mongo.db.exercises.find())
        return exercises

    @ns.expect(exercise_schema)
    @ns.marshal_with(exercise_schema, code=201)
    def post(self):
        """
        Adiciona um novo dado à lista de exercício
        """
        new_exercise = request.get_json()
        exercise = mongo.db.exercises.insert_one(new_exercise)
        return mongo.db.exercises.find_one({'_id': exercise.inserted_id})

# api.add_namespace(ns)
