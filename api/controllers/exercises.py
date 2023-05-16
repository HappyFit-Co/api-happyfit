from flask import abort, jsonify
from api.services.exercises import ExerciseService

class ExerciseController: 
    def __init__(self):
        self.exercise_service = ExerciseService()

    def get_all_exercises(self):
        exercises = self.exercise_service.get_all_exercises()
        if not exercises:
            return exercises, 404
        return exercises, 200

    def get_exercise_by_id(self, exercise_id):
        exercise = self.exercise_service.get_exercise_by_id(exercise_id)
        if not exercise:
            return exercise, 404
        return exercise, 200

    def get_exercise_by_name(self, exercise_name):
        exercises = self.exercise_service.get_exercise_by_name(exercise_name)
        if not exercises:
            return exercises, 404
        return exercises, 200

    def get_exercise_by_target(self, exercise_target):
        exercises = self.exercise_service.get_exercise_by_target(exercise_target)
        if not exercises:
            return exercises, 404
        return exercises, 200
