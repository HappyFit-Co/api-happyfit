from bson.objectid import ObjectId

from api.schemas.goals import default_goal
from api.utils.database import mongo

class GoalService:
    # Métodos de CRUD GOAL
    def get_goal(user_id):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            return user["goal"], None
        except:
            return None, 'Erro interno ao manipular dados no serviço'

    def edit_goal(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"goal": data}}
            )
            return data, None
        except:
            return None, 'Erro interno ao manipular dados no serviço'

    def delete_goal(user_id):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"goal": default_goal}}
            )
            return None
        except:
            return 'Erro interno ao manipular dados no serviço'

    # Métodos de adicição e remoção

    def add_exercise(user_id, data):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            
            if user:
                workout_goals = user.get("goal", {}).get("workout", [])
                
                if data not in workout_goals:
                    mongo.db.users.update_one(
                        {"_id": ObjectId(user_id)},
                        {"$push": {"goal.workout": data}}
                    )
                else:
                    return None, 'Os dados já existem, evite redundância'
                
            return None, None
        except:
            return 'Erro interno ao manipular dados no serviço', None

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
            return None
        except:
            return 'Erro interno ao manipular dados no serviço'

    def add_food(user_id, data):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            
            if user:
                diet_goals = user.get("goal", {}).get("diet", [])
                
                if data not in diet_goals:
                    mongo.db.users.update_one(
                        {"_id": ObjectId(user_id)},
                        {"$push": {"goal.diet": data}}
                    )
                else:
                    return None, 'Os dados já existem, evite redundância'
                
            return None, None
        except:
            return 'Erro interno ao manipular dados no serviço', None

    def rmv_food(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$pull": {"goal.diet": {
                    "food_id": data["food_id"],
                    "weekday": data["weekday"]
                }}}
            )
            return None
        except:
            return 'Erro interno ao manipular dados no serviço'
