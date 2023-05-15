from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource

from api.controllers.notifications import NotificationController
from api.schemas.notificationSchema import notification_schema, ns


@ns.route('/')
class Notifications(Resource):
    @jwt_required()
    @ns.doc(description='Obtem todas configurações de notificação do usuário')
    def get(self):
        """Lista configurações de notificação."""
        return NotificationController.get_notificationsConfigs(get_jwt_identity())


@ns.route('/workout')
class NotificationsWorkout(Resource):
    @jwt_required()
    @ns.expect(notification_schema)
    @ns.doc(description='Altera as configurações de notificação de treino do usuário')
    def put(self):
        """Altera configurações de notificação de treino."""
        pass


@ns.route('/workout/default')
class NotificationsWorkoutDefault(Resource):
    @jwt_required()
    @ns.doc(description='Altera as configurações de notificação do usuário para padrão')
    def put(self):
        """Altera configurações de notificação de treino para padrão."""
        pass


@ns.route('/water')
class NotificationsWater(Resource):
    @jwt_required()
    @ns.expect(notification_schema)
    @ns.doc(description='Altera as configurações de notificação de água do usuário para padrão')
    def put(self):
        """Altera configurações de notificação de água."""
        pass


@ns.route('/water/default')
class NotificationsWaterDefault(Resource):
    @jwt_required()
    @ns.doc(description='Altera as configurações de notificação do usuário para padrão')
    def put(self):
        """Altera configurações de notificação de água de treino para padrão."""
        pass
