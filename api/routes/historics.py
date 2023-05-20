from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource

from api.controllers.historics import HistoricController
from api.schemas.historics import ns


@ns.route('/')
class Historic(Resource):
    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Retorna o histórico do usuário')
    def get(self):
        """Retorna o histórico do usuário"""
        return HistoricController.get_historic(get_jwt_identity())

    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Limpa todo o histórico do usuário')
    def delete(self):
        """Apaga o histórico do usuário"""
        return HistoricController.delete_historic(get_jwt_identity())
