from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource

from api.controllers.historics import HistoricController
from api.schemas.historics import ns
from api.schemas.users import user_schema
from api.schemas.response import (
    delete_sucess_schema,
    unauthorized_schema,
    unprocessable_schema,
    internal_server_schema
)

@ns.route('/')
class Historic(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna o histórico do usuário')
    @ns.response(200, 'Sucesso', user_schema['historic'])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self):
        """Retorna o histórico do usuário"""
        return HistoricController.get_historic(get_jwt_identity())

    @jwt_required()
    @ns.doc(security='jwt', description='Limpa todo o histórico do usuário')
    @ns.response(200, 'Sucesso', delete_sucess_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def delete(self):
        """Apaga o histórico do usuário"""
        return HistoricController.delete_historic(get_jwt_identity())
