from api.utils.database import mongo
from bson.objectid import ObjectId

class UserService: 
    def create_user(self, user_data):
        try:
            result = mongo.db.users.insert_one(user_data)
            return result.inserted_id
        except TypeError:
            return None
 
    def get_user_by_id(self, user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return user

    def get_user_by_email(self, user_email):
        user = list(mongo.db.users.find({"email": {"$regex": user_email, "$options": "i"}}))
        return user