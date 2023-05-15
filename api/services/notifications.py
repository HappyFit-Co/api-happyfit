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
            return {'message': 'Erro ao buscar configuração'}, 500
