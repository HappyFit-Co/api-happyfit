from flask_jwt_extended import create_access_token
from flask_restx import abort, marshal

from api.schemas.users import user_schema
from api.security.password import compare_pwd
from api.security.token import create_token, is_token_valid
from api.services.users import UserService


class UserController:
    def get_user_me(self, user_id):
        if not user_id:
            abort(401, description='Usuário não encontrado')
        
        user = UserService.get_user_by_id(user_id)

        return user

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
    
    def set_user(user_id):
        error = RecordService.add_workout_record(user_id, exercise)
        if error:
            return {'msg': error}, 404
        return {'msg': 'Success in adding exercise'}, 200
