from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource, marshal_with

from api.controllers.notifications import NotificationController
from api.schemas.notifications import (notification_schema, ns,
                                            water_schema, workout_schema)

@ns.route('/')
class Notifications(Resource):
    @jwt_required()    
    @ns.doc(security='jwt', description='Obtem todas configurações de notificação do usuário')
    @marshal_with(notification_schema)
    def get(self):
        """Lista configurações de notificação."""
        return NotificationController.get_notifications_configs(get_jwt_identity())


@ns.route('/workout')
class NotificationsWorkout(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Altera as configurações de notificação de treino do usuário')
    @ns.expect(workout_schema)
    def put(self):
        """Altera configurações de notificação de treino."""
        return NotificationController.set_notification_workout(get_jwt_identity(), request.json)
        


@ns.route('/workout/default')
class NotificationsWorkoutDefault(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Altera as configurações de notificação do usuário para padrão')
    def put(self):
        """Altera configurações de notificação de treino para padrão."""
        return NotificationController.set_notification_workout_default(get_jwt_identity())


@ns.route('/water')
class NotificationsWater(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Altera as configurações de notificação de água do usuário para padrão')
    @ns.expect(water_schema)
    def put(self):
        """Altera configurações de notificação de água."""
        return NotificationController.set_notification_water(get_jwt_identity(), request.json)


@ns.route('/water/default')
class NotificationsWaterDefault(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Altera as configurações de notificação do usuário para padrão')
    def put(self):
        """Altera configurações de notificação de água de treino para padrão."""
        return NotificationController.set_notification_water_default(get_jwt_identity())
