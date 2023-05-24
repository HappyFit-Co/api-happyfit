from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource

from api.controllers.notifications import NotificationController
from api.schemas.notifications import (
    ns,
    notification_schema, 
    water_schema,
    workout_schema
)
from api.schemas.response import (
    update_sucess_schema,
    unauthorized_schema,
    bad_request_schema,
    not_found_schema,
    unprocessable_schema,
    internal_server_schema
)

@ns.route('/')
class Notifications(Resource):
    @jwt_required()    
    @ns.doc(security='jwt', description='Obtem todas configurações de notificação do usuário')
    @ns.response(200, 'Sucesso', notification_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self):
        """Lista configurações de notificação"""
        return NotificationController.get_notifications_configs(get_jwt_identity())

@ns.route('/workout')
class NotificationsWorkout(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Altera as configurações de notificação de treino do usuário')
    @ns.expect(workout_schema)
    @ns.response(200, 'Sucesso', update_sucess_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def put(self):
        """Altera configurações de notificação de treino"""
        return NotificationController.set_notification_workout(get_jwt_identity(), ns.payload)
        
@ns.route('/workout/default')
class NotificationsWorkoutDefault(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Altera as configurações de notificação de treino do usuário para padrão')
    @ns.response(200, 'Sucesso', update_sucess_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def put(self):
        """Altera configurações de notificação de treino para padrão"""
        return NotificationController.set_notification_workout_default(get_jwt_identity())

@ns.route('/water')
class NotificationsWater(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Altera as configurações de notificação de água do usuário')
    @ns.expect(water_schema)
    @ns.response(200, 'Sucesso', update_sucess_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def put(self):
        """Altera configurações de notificação de água"""
        return NotificationController.set_notification_water(get_jwt_identity(), ns.payload)
    
@ns.route('/water/default')
class NotificationsWaterDefault(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Altera as configurações de notificação de água do usuário para padrão')
    @ns.response(200, 'Sucesso', update_sucess_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def put(self):
        """Altera configurações de notificação de água para padrão"""
        return NotificationController.set_notification_water_default(get_jwt_identity())
