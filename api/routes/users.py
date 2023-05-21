from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource

from api.utils.validate import validate_request
from api.controllers.users import UserController
from api.schemas.users import (
    ns,
    user_schema,
    create_user_schema, 
    login_user_schema
)
from api.schemas.response import (
    update_sucess_schema,
    delete_sucess_schema,
    login_sucess_schema,
    unauthorized_schema,
    invalid_credentials_schema,
    bad_request_schema,
    not_found_schema,
    unprocessable_schema,
    internal_server_schema
)

@ns.route('/')
class UserMe(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna as informações do usuário logado')
    @ns.response(200, 'Sucesso', user_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self):
        """Lista o usuário logado"""
        return UserController.get_user_me(get_jwt_identity())

    @ns.doc(description='Registra um novo usuário')
    @ns.expect(create_user_schema)
    @ns.response(201, 'Criado', user_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def post(self):
        """Cadastra um novo usuário"""
        return UserController.create_user(validate_request(ns.payload, create_user_schema))
    
    @jwt_required()
    @ns.doc(security='jwt', description='Altera dados do seu usuário')
    @ns.expect(create_user_schema)
    @ns.response(200, 'Sucesso', update_sucess_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def put(self):
        """Edita o seu usuário"""
        return UserController.update_user(get_jwt_identity(), validate_request(ns.payload, create_user_schema))
    
    @jwt_required()
    @ns.doc(security='jwt', description='Deleta dados do seu usuário')
    @ns.response(200, 'Sucesso', delete_sucess_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def delete(self):
        """Exclui o seu usuário"""
        return UserController.delete_user(get_jwt_identity())

@ns.route('/login')
class LoginUser(Resource):
    @ns.doc(description='Login do usuário')
    @ns.expect(login_user_schema)
    @ns.response(200, 'Sucesso', login_sucess_schema)
    @ns.response(401, 'Não autorizado', invalid_credentials_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def post(self):
        """Faz login do usuário"""
        return UserController.login(validate_request(ns.payload, login_user_schema)) 
