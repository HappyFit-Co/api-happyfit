from api.services.users import UserService

class UserController: 
    def __init__(self):
        self.user_service = UserService()

    def get_user_me(self, user_id):
        pass

    def create_user(self, user_data):
        created_user_id = self.user_service.create_user(user_data)
        if not created_user_id:
            return user, 400 
        user = self.user_service.get_user_by_id(created_user_id)
        if not user:
            return user, 404
        return user, 201 

    def get_user_by_email(self, user_email):
        pass


