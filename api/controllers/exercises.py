from flask_restx import marshal

from api.services.exercises import ExerciseService
from api.schemas.exercises import exercise_schema

class ExerciseController: 
    def get_all_exercises():
        exercises, error = ExerciseService.get_all_exercises()
        if error:
            return {'msg': error}, 500
        if not exercises:
            return [], 404
        return marshal(exercises, exercise_schema), 200

    def get_exercise_by_id(exercise_id):
        exercise, error = ExerciseService.get_exercise_by_id(exercise_id)
        if error:
            return {'msg': error}, 500
        if not exercise:
            return {'msg': "No data was found"}, 404
        return marshal(exercise, exercise_schema), 200
        
    def get_exercise_by_name(exercise_name):
        exercises, error = ExerciseService.get_exercise_by_name(exercise_name)
        if error:
            return {'msg': error}, 500
        if not exercises:
            return [], 404
        return marshal(exercises, exercise_schema), 200

    def get_exercise_by_target(exercise_target):
        exercises, error = ExerciseService.get_exercise_by_target(exercise_target)
        if error:
            return {'msg': error}, 500
        if not exercises:
            return [], 404
        return marshal(exercises, exercise_schema), 200
