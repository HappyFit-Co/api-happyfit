from flask_jwt_extended import create_access_token
from flask_restx import abort

from api.security.password import compare_pwd
from api.security.token import create_token, is_token_valid
from api.services.users import UserService as user_service


class UserController:

    def get_user_me(self, user_id):
        if not user_id:
            abort(401, description='Usuário não encontrado')
        
        user = user_service.get_user_by_id(user_id)

        return user

    def create_user(self, user_data):
        created_user_id = self.user_service.create_user(user_data)
        if not created_user_id:
            return user, 400
        user = self.user_service.get_user_by_id(created_user_id)
        if not user:
            return user, 404
        return user, 201

    def login(self, request):
        credentials = request.json
        email = credentials['email']
        password = credentials['pwd']

        user = self.get_user_by_email(email)

        if not user:
            return {'message': 'Usuário não encontrado'}, 401
        
        if not compare_pwd(password, user['pwd']):
            return {'message': 'Senha incorreta'}, 401

        access_token = create_token(user['_id'])
        
        access_token = create_access_token(identity=str(user['_id']), )
        return {'access_token': access_token}
    
    def get_user_by_email(self, user_email):
        return user_service.get_user_by_email(user_email)
