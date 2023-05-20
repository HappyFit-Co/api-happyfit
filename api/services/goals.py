from bson.objectid import ObjectId

from api.schemas.goals import default_goal
from api.utils.database import mongo


class GoalService:
    # Métodos de CRUD GOAL
    def get_goal(user_id):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            return user["goal"]
        except:
            return {'msg': 'Error to return goal'}, 500

    def edit_goal(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"goal": data}}
            )
            return data
        except:
            return {'msg': 'Error to update goal'}, 500

    def delete_goal(user_id):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"goal": {}}}
            )
            return {'msg': 'Goal successfully deleted'}, 200
        except:
            return {'msg': 'Error to delete goal'}, 500

    # Métodos de adicição e remoção

    def add_exercise(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$push": {"goal.workout": data}}
            )
            return {'msg': 'Exercise successfully added'}, 200
        except:
            return {'msg': 'Error to add exercise record'}, 500

    def rmv_exercise(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$pull": {"goal.workout": {
                    "exercise_id": data["exercise_id"],
                    "hour": data["hour"],
                    "weekday": data["weekday"]
                    }}}
            )
            return {'msg': 'Exercise successfully removed'}, 200
        except:
            return {'msg': 'Error to remove exercise record'}, 500

    def add_food(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$push": {"goal.diet": data}}
            )
            return {'msg': 'Food successfully added'}, 200
        except:
            return {'msg': 'Error to add food record'}, 500

    def rmv_food(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$pull": {"goal.diet": {
                    "food_id": data["food_id"],
                    "weekday": data["weekday"]
                }}}
            )
            return {'msg': 'Food successfully removed'}, 200
        except:
            return {'msg': 'Error to remove food record'}, 500
