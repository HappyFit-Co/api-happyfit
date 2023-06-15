from bson.objectid import ObjectId

from api.utils.database import mongo

class HistoricService: 
    def get_historic(user_id):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            return user["historic"], None
        except:
            return None, 'Erro interno ao manipular dados no serviço'

    def clear_historic(user_id):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"historic": [] }}
            )
            return None
        except:
            return 'Erro interno ao manipular dados no serviço'
        