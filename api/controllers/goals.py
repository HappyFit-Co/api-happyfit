from flask_restx import marshal

from api.schemas.goals import goal_schema
from api.services.goals import GoalService


class GoalController:
    def get_goal(user_id):
        response = GoalService.get_goal(user_id)
        
        # Caso seja erro 500
        if isinstance(response, tuple):
            return response
        
        # Caso não retorne dados
        if not response:
            return {}, 404

        return marshal(response, goal_schema), 200

    def post_goal(user_id, data):
        response = GoalService.edit_goal(user_id, data)

        if isinstance(response, tuple):
            return response

        if not response:
            return {}, 404
        
        return marshal(response, goal_schema), 200 

    def put_goal(user_id, data):
        response = GoalService.edit_goal(user_id, data)

        if isinstance(response, tuple):
            return response

        if not response:
            return {}, 404
        return marshal(response, goal_schema), 200


    def delete_goal(user_id):
        return GoalService.delete_goal(user_id)
    

    def add_exercise(user_id, exercise_register):
        print(exercise_register)
        return GoalService.add_exercise(user_id, exercise_register)
    
    def rmv_exercise(user_id, exercise_id):
        return GoalService.rmv_exercise(user_id, exercise_id)

    def add_food(user_id, food_register):
        return GoalService.add_food(user_id, food_register)
    
    def rmv_food(user_id, food_register):
        return GoalService.rmv_food(user_id, food_register)