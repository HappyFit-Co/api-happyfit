import bcrypt
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource

from api.controllers.users import UserController
from api.schemas.users import ns, user_schema
from api.security.password import compare_pwd

user_controller = UserController()


@ns.route('/')
class UserMe(Resource):
    @jwt_required()
    @ns.doc(description='Retorna as informações do usuário logado')
    @ns.marshal_with(user_schema)
    def get(self):
        """Lista o usuário logado"""
        return user_controller.get_user_me(get_jwt_identity())

    @ns.doc(description='Registra um novo usuário')
    @ns.expect(user_schema)
    @ns.marshal_with(user_schema)
    def post(self):
        """Cadastra um novo usuário"""
        return user_controller.create_user(request.json)


@ns.route('/login')
class LoginUser(Resource):
    @ns.doc(description='Login do usuário')
    @ns.expect(user_schema)
    def post(self):
        """Faz login do usuário"""
        return user_controller.login(request)
