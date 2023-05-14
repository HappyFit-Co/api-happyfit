from api.utils.database import mongo

class ExerciseService:
    def get_all_exercises(self):
        exercises = list(mongo.db.exercises.find())
        return exercises

    def add_new_exercise(self, new_exercise):
        exercise = mongo.db.exercises.insert_one(new_exercise)
        return mongo.db.exercises.find_one({'_id': exercise.inserted_id})
