from api.services.exercises import ExerciseService

class ExerciseController:
    def __init__(self):
        self.exercise_service = ExerciseService()

    def get_all_exercises(self):
        exercises = self.exercise_service.get_all_exercises()
        return exercises

    def get_exercise_by_id(self, exercise_id):
        exercise = self.exercise_service.get_exercise_by_id(exercise_id)
        return exercise

    def get_exercise_by_name(self, exercise_name):
        exercises = self.exercise_service.get_exercise_by_name(exercise_name)
        return exercises

    def get_exercise_by_target(self, exercise_target):
        exercises = self.exercise_service.get_exercise_by_target(exercise_target)
        return exercises
