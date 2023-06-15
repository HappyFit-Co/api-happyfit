from flask_restx import marshal

from api.services.notifications import NotificationService
from api.schemas.notifications import (
    notification_schema, 
    default_notification_config, 
    water_schema, 
    workout_schema
)
from api.utils.validate import validate_data

class NotificationController:
    def get_notifications_configs(user_id):
        user, error = NotificationService.get_config(user_id)
        if error:
            return {'msg': error}, 500
        if not user:
            return {'msg': 'Nenhum dado encontrado'}, 404
        
        notification = user["notification_config"]
        if not user:
            return {'msg': 'Nenhum dado encontrado'}, 404
        
        return marshal(notification, notification_schema), 200

    def set_notification_workout(user_id, data):
        newConfig, error = validate_data(data, workout_schema)
        if error:
            return {'msg': error}, 400
        
        error = NotificationService.set_workout_config(user_id, newConfig)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Atualizado com sucesso'}, 200
    

    def set_notification_workout_default(user_id):
        defaultWorkoutConfig = default_notification_config['workout']
    
        error = NotificationService.set_workout_config(user_id, defaultWorkoutConfig)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Atualizado com sucesso'}, 200
    

    def set_notification_water(user_id, data):
        newConfig, error = validate_data(data, water_schema)
        if error:
            return {'msg': error}, 400
        
        error = NotificationService.set_water_config(user_id, newConfig)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Atualizado com sucesso'}, 200

    def set_notification_water_default(user_id):
        defaultWaterConfig = default_notification_config['water']
    
        error = NotificationService.set_water_config(user_id, defaultWaterConfig)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Atualizado com sucesso'}, 200
