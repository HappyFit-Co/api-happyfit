from flask import request
from flask_restx import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from api.controllers.records import RecordController
from api.schemas.records import (
    ns,
    record_schema,
    create_record_schema,
    bad_request_schema,
    unauthorized_schema,
    not_found_schema,
    unprocessable_schema
)

@ns.route('/')
class UserMe(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna registro do dia.')
    @ns.response(200, 'Sucesso', record_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    def get(self):
        """Lista todo registro do dia"""
        return RecordController.get_daily_record(get_jwt_identity())
    
    @jwt_required()
    @ns.doc(security='jwt', description='Criar registro do dia.')
    @ns.response(201, 'Criado', record_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.expect(create_record_schema)
    def post(self):
        """Registra as atividade do dia"""
        return RecordController.create_record(get_jwt_identity(), request.json)

