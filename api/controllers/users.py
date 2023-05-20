from flask_jwt_extended import create_access_token
from flask_restx import abort, marshal

from api.schemas.users import user_schema
from api.security.password import compare_pwd
from api.security.token import create_token, is_token_valid
from api.services.users import UserService


class UserController:
    def get_user_me(self, user_id):
        user = UserService.get_user_by_id(user_id)
        return marshal(user, user_schema), 200

    def create_user(self, user_data):
        created_user_id = UserService.create_user(user_data)
        if not created_user_id:
            return {"msg": "E-mail já em uso"}, 400
        
        new_user = UserService.get_user_by_id(created_user_id)

        if not new_user:
            return {"msg": "Erro ao criar usuário"}, 404
        
        return marshal(new_user, user_schema), 201

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
        return UserService.get_user_by_email(user_email)
    
    def edit_user(self, user_id, user):
        UserService.edit_user(user_id, user)
        return {'msg': 'User updated successfully'}, 200
    
    def delete_user(self, user_id):
        UserService.delete_user(user_id)
        return {'msg': 'User deleted successfully'}, 200
