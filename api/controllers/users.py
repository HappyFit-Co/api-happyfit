from flask_jwt_extended import create_access_token
from flask_restx import abort, marshal

from api.schemas.goals import default_goal
from api.schemas.notifications import default_notification_config
from api.schemas.users import user_schema
from api.security.password import encrypt_pwd, compare_pwd
from api.security.token import create_token, is_token_valid
from api.services.users import UserService


class UserController:
    def get_user_me(user_id):
        user, error = UserService.get_user_by_id(user_id)
        if error:
            return {'msg': error}, 500
        if not user:
            return {'msg': "No data was found"}, 404
        return marshal(user, user_schema), 200

    def create_user(user_data):
        # Criptografando senha do usuário
        password = user_data.get('pwd')
        hashed_password = encrypt_pwd(password)
        user_data['pwd'] = hashed_password

        # Verifica se o email já está em uso
        existing_user, error = UserService.get_user_by_email(user_data["email"])
        if error:
            return {'msg': error}, 500
        if existing_user:
            return {'msg': "Email is already being used"}, 400

        # Define os campos padrão
        user_data.setdefault("goal", default_goal)
        user_data.setdefault("historic", [])
        user_data.setdefault("notification_config", default_notification_config)

        # Cria novo usuário
        created_user_id, error = UserService.create_user(user_data)
        if error:
            return {'msg': error}, 500
        
        # Verifica se foi mesmo criado
        new_user, error = UserService.get_user_by_id(created_user_id)
        if error:
            return {'msg': error}, 500
        if not new_user:
            return {'msg': "No data was found"}, 404
        return marshal(new_user, user_schema), 201

    def login(credentials):
        email = credentials['email']
        password = credentials['pwd']

        user, error = UserService.get_user_by_email(email)
        if error:
            return {'msg': error}, 500
        if not user:
            return {'msg': 'Invalid user credentials'}, 401
        if not compare_pwd(password, user['pwd']):
            return {'msg': 'Invalid user credentials'}, 401

        access_token = create_token(user['_id'])
        return {'access_token': access_token}
    
    def update_user(user_id, user):    
        existing_user, error = UserService.get_user_by_email(user["email"])
        if error:
            return {'msg': error}, 500

        if existing_user and str(existing_user["_id"]) != str(user_id):
            return {'msg': "Email is already being used"}, 400
        
        user["pwd"] = encrypt_pwd(user["pwd"])
        
        error = UserService.update_user(user_id, user)
        if error:
            return {'msg': error}, 500
        return {'msg': "Successfully updated"}, 200
    
    def delete_user(user_id):
        error = UserService.delete_user(user_id)
        if error:
            return {'msg': error}, 500
        return {'msg': "Successfully deleted"}, 200
