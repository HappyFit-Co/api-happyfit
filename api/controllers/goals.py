from flask_restx import marshal

from api.schemas.goals import goal_schema
from api.services.goals import GoalService

class GoalController:
    def get_goal(user_id):
        goal, error = GoalService.get_goal(user_id)
        if error:
            return {'msg': error}, 500
        if not goal:
            return {'msg': "No data was found"}, 404
        return marshal(goal, goal_schema), 200

    def post_goal(user_id, data):
        goal, error = GoalService.edit_goal(user_id, data)
        if error:
            return {'msg': error}, 500
        if not goal:
            return {'msg': "No data was found"}, 404
        return marshal(goal, goal_schema), 201

    def put_goal(user_id, data):
        goal, error = GoalService.edit_goal(user_id, data)
        if error:
            return {'msg': error}, 500
        if not goal:
            return {'msg': "No data was found"}, 404
        return marshal(goal, goal_schema), 200

    def delete_goal(user_id):
        error = GoalService.delete_goal(user_id)
        if error:
            return {'msg': error}, 500
        return {'msg': "Successfully deleted"}, 200

    def add_exercise(user_id, exercise_register):
        error, redundancy = GoalService.add_exercise(user_id, exercise_register)
        if error:
            return {'msg': error}, 500
        if redundancy:
            return {'msg': redundancy}, 400
        return {'msg': 'Successfully added'}, 200

    def rmv_exercise(user_id, exercise_register):
        error = GoalService.rmv_exercise(user_id, exercise_register)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Successfully deleted'}, 200

    def add_food(user_id, food_register):
        error, redundancy = GoalService.add_food(user_id, food_register)
        if error:
            return {'msg': error}, 500
        if redundancy:
            return {'msg': redundancy}, 400
        return {'msg': 'Successfully added'}, 200

    def rmv_food(user_id, food_register):
        error = GoalService.rmv_food(user_id, food_register)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Successfully deleted'}, 200
