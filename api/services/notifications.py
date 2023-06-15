from bson.objectid import ObjectId

from api.utils.database import mongo

class NotificationService:
    def get_config(user_id):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            return user, None
        except:
            return None, 'Erro interno ao manipular dados no serviço'

    def set_workout_config(user_id, newConfig):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"notification_config.workout": newConfig}}
            )
            return None
        except:
            return 'Erro interno ao manipular dados no serviço'

    def set_water_config(user_id, newConfig):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"notification_config.water": newConfig}}
            )
            return None
        except:
            return 'Erro interno ao manipular dados no serviço'
