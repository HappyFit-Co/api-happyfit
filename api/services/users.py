import bcrypt
from bson.objectid import ObjectId

from api.schemas.goals import default_goal
from api.schemas.notifications import default_notification_config
from api.security.password import encrypt_pwd
from api.utils.database import mongo


class UserService: 
    def create_user(user_data):
        try:
            # Criptografando senha do usuário
            password = user_data.get('pwd')
            hashed_password = encrypt_pwd(password)
            user_data['pwd'] = hashed_password

            # Verifica se o e-mail já está em uso
            existing_user = mongo.db.users.find_one({"email": user_data["email"]})
            if existing_user:
                return None

            # Define os campos padrão
            user_data.setdefault("goal", default_goal)
            user_data.setdefault("historic", [])
            user_data.setdefault("notification_config", default_notification_config)

            result = mongo.db.users.insert_one(user_data)
            return result.inserted_id
        except:
            return None

    def get_user_by_id(user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return user

    def get_user_by_email(user_email):
        user = mongo.db.users.find_one({"email": user_email})
        return user
        
    def edit_user(user_id, edited_user):
        query = {"_id": ObjectId(user_id)}
        update = {
            "$set": {
                "name": edited_user.get("name"),
                "email": edited_user.get("email"),
                "pwd": edited_user.get("pwd"),
                "weight": edited_user.get("weight"),
                "height": edited_user.get("height"),
                "birthday": edited_user.get("birthday"),
                "activity_level": edited_user.get("activity_level")
            }
        }
        mongo.db.users.update_one(query, update)
        
    def delete_user(user_id):
        mongo.db.users.delete_one({"_id": ObjectId(user_id)})


        