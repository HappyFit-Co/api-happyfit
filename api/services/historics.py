from bson.objectid import ObjectId

from api.utils.database import mongo


class HistoricService: 
    def get_historic(user_id):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            return user["historic"]
        except:
            return {'msg': 'Error to return historic'}, 500

    def clear_historic(user_id):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"historic": [] }}
            )
            return {'msg': 'Historic successfully deleted'}, 200
        except:
            return {'msg': 'Error to delete historic'}, 500