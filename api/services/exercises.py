from api.utils.database import mongo
from bson.objectid import ObjectId 

class ExerciseService:
    def get_all_exercises():
        try:
            exercises = list(mongo.db.exercises.find())
            return exercises, None
        except:
            return None, "Internal error handling data in service"

    def get_exercise_by_id(exercise_id):
        try:
            exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
            return exercise, None
        except:
            return None, "Internal error handling data in service"
        
    def get_exercise_by_name(exercise_name):
        try:
            exercises = list(mongo.db.exercises.find({"name": {"$regex": exercise_name, "$options": "i"}}))
            return exercises, None
        except:
            return None, "Internal error handling data in service"
        
    def get_exercise_by_target(exercise_target):
        try:
            exercises = list(mongo.db.exercises.find({"target": {"$regex": exercise_target, "$options": "i"}}))
            return exercises, None
        except:
            return None, "Internal error handling data in service"
