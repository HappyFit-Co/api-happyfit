from api.services.notifications import \
    NotificationService as notification_service


class NotificationController: 
    def get_notificationsConfigs(user_id):
        notificationsConfig = notification_service.get_config(user_id)
        return notificationsConfig