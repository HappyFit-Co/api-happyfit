import bcrypt
from bson.objectid import ObjectId

from api.security.password import encrypt_pwd
from api.utils.database import mongo


class UserService: 
    def create_user(user_data):
        try:
            result = mongo.db.users.insert_one(user_data)
            return result.inserted_id, None
        except:
            return None, "Internal error handling data in service"

    def get_user_by_id(user_id):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            return user, None
        except:
            return None, "Internal error handling data in service"

    def get_user_by_email(user_email):
        try:
            user = mongo.db.users.find_one({"email": user_email})
            return user, None
        except:
            return None, "Internal error handling data in service"
        
    def update_user(user_id, edited_user):
        try:
            query = {"_id": ObjectId(user_id)}
            update = {
                "$set": {
                    "name": edited_user.get("name"),
                    "email": edited_user.get("email"),
                    "pwd": edited_user.get("pwd"),
                    "weight": edited_user.get("weight"),
                    "height": edited_user.get("height"),
                    "birthday": edited_user.get("birthday"),
                    "sex": edited_user.get("sex"),
                    "activity_level": edited_user.get("activity_level")
                }
            }
            mongo.db.users.update_one(query, update)
            return None
        except:
            return "Internal error handling data in service"
        
    def delete_user(user_id):
        try:
            mongo.db.users.delete_one({"_id": ObjectId(user_id)})
            return None
        except:
            return "Internal error handling data in service"
              