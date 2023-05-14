from api.services.exercises import ExerciseService

class ExerciseController:
    def __init__(self):
        self.exercise_service = ExerciseService()

    def get_all_exercises(self):
        exercises = self.exercise_service.get_all_exercises()
        return exercises

    def add_new_exercise(self, new_exercise):
        exercise = self.exercise_service.add_new_exercise(new_exercise)
        return exercise
