from bson.objectid import ObjectId
from flask_restx import abort

from api.utils.database import mongo


class NotificationService:
    def get_config(user_id):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            if not user:
                abort(404, "Usuário não encontrado")
            return user["notification_config"], 200
        except:
            abort(400, "Usuário não encontrado")

    def set_workout_config(user_id, newConfig):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"notification_config.workout": newConfig}}
            )
            return {"message": "Configuração atualizada com sucesso"}, 200
        except:
            return {'message': 'Erro ao atualizar configuração'}, 400

    def set_water_config(user_id, newConfig):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"notification_config.water": newConfig}}
            )
            return {"message": "Configuração atualizada com sucesso"}, 200
        except:
            return {'message': 'Erro ao atualizar configuração'}, 400
