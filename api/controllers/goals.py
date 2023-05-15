from api.services.goals import GoalService

class GoalController: 
    def __init__(self):
        self.goal_service = GoalService()