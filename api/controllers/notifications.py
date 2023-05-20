from flask import jsonify

from api.services.notifications import NotificationService


class NotificationController:
    def get_notifications_configs(user_id):
        notificationsConfig = NotificationService.get_config(user_id)
        return notificationsConfig

    def set_notification_workout(user_id, newConfig):
        status = NotificationService.set_workout_config(user_id, newConfig)
        return status

    def set_notification_workout_default(user_id):
        defaultWorkoutConfig = {
            "frequency": "every weekday",
            "hour": "17:00"
        }
        status = NotificationService.set_workout_config(user_id, defaultWorkoutConfig)
        return status

    def set_notification_water(user_id, newConfig):
        status = NotificationService.set_water_config(user_id, newConfig)
        return status

    def set_notification_water_default(user_id):
        defaultWaterConfig = {
            "frequency": "hourly",
            "start_hour": "08:00",
            "end_hour": "20:00"
        }
        status = NotificationService.set_water_config(user_id, defaultWaterConfig)
        return status
