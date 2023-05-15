import bcrypt
from bson.objectid import ObjectId

from api.security.password import encrypt_pwd
from api.utils.database import mongo


class UserService: 
    def create_user(user_data):
        try:
            # Criptografando senha do usuário
            password = user_data.get('pwd')
            hashed_password = encrypt_pwd(password)
            user_data['pwd'] = hashed_password
            
            result = mongo.db.users.insert_one(user_data)
            return result.inserted_id
        except TypeError:
            return None
 
    def get_user_by_id(user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return user

    def get_user_by_email(user_email):
        user = mongo.db.users.find_one({"email": user_email})
        return user