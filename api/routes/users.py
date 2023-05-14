from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from api.controllers.userController import UserController
from api.schemas.userSchema import ns, user_schema

user_controller = UserController()

@ns.route('/')
class UserMe(Resource):
    @jwt_required()
    @ns.doc(description='Retorna as informações do usuário logado')
    @ns.marshal_with(user_schema)
    def get(self):
        """Lista o usuário logado"""
        user_id = get_jwt_identity()
        return user_controller.GetUserMe(user_id)
    
    @ns.doc(description='Registra um novo usuário')
    @ns.expect(user_schema)
    @ns.marshal_with(user_schema)
    def post(self):
        """Cadastra um novo usuário"""
        user_data = request.json
        new_user = user_controller.create_user(user_data)
        return new_user, 201
    
@ns.route('/login')
class LoginUser(Resource):
    @ns.doc(description='Login do usuário')
    @ns.expect(user_schema)
    def post(self):
        """Faz login do usuário"""
        credentials = request.json
        email = credentials['email']
        password = credentials['pwd']
        user = user_controller.get_user_by_email(email)
        if not user:
            return {'message': 'Usuário não encontrado'}, 401
        if not user_controller.check_password(user['pwd'], password):
            return {'message': 'Senha incorreta'}, 401
        access_token = create_access_token(identity=str(user['_id']))
        return {'access_token': access_token}
