from api.services.notifications import NotificationService

class NotificationController:
    def __init__(self):
        self.notification_service = NotificationService()