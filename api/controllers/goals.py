from flask_restx import marshal

from api.schemas.goals import goal_schema
from api.services.goals import GoalService


class GoalController:
    def get_goal(user_id):
        goal = GoalService.get_goal(user_id)
        return marshal(goal, goal_schema)

    def post_goal(user_id, data):
        return GoalService.edit_goal(user_id, data)

    def put_goal(user_id, data):
        return GoalService.edit_goal(user_id, data)

    def delete_goal(user_id):
        return GoalService.delete_goal(user_id)
    

    def add_exercise(user_id, exercise_register):
        return GoalService.add_exercise(user_id, exercise_register)
    
    def rmv_exercise(user_id, exercise_id):
        return GoalService.rmv_exercise(user_id, exercise_id)

