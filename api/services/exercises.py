from api.utils.database import mongo
from bson.objectid import ObjectId 

class ExerciseService:
    def get_all_exercises(self):
        exercises = list(mongo.db.exercises.find())
        return exercises

    def get_exercise_by_id(self, exercise_id):
        exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
        return exercise

    def get_exercise_by_name(self, exercise_name):
        exercises = list(mongo.db.exercises.find({"name": {"$regex": exercise_name, "$options": "i"}}))
        return exercises

    def get_exercise_by_target(self, exercise_target):
        exercises = list(mongo.db.exercises.find({"target": {"$regex": exercise_target, "$options": "i"}}))
        return exercises
