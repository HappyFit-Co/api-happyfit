from flask_restx import marshal

from api.schemas.goals import (
    goal_schema,
    workout_schema,
    diet_schema
)
from api.services.goals import GoalService
from api.utils.validate import validate_data

class GoalController:
    def get_goal(user_id):
        goal, error = GoalService.get_goal(user_id)
        if error:
            return {'msg': error}, 500
        if not goal:
            return {'msg': 'Nenhum dado encontrado'}, 404
        return marshal(goal, goal_schema), 200

    def post_goal(user_id, data):
        goal_register, error = validate_data(data, goal_schema)
        if error:
            return {'msg': error}, 400
        
        goal, error = GoalService.edit_goal(user_id, goal_register)
        if error:
            return {'msg': error}, 500
        if not goal:
            return {'msg': 'Nenhum dado encontrado'}, 404
        return marshal(goal, goal_schema), 201

    def put_goal(user_id, data):
        goal_register, error = validate_data(data, goal_schema)
        if error:
            return {'msg': error}, 400
        
        goal, error = GoalService.edit_goal(user_id, goal_register)
        if error:
            return {'msg': error}, 500
        if not goal:
            return {'msg': 'Nenhum dado encontrado'}, 404
        return marshal(goal, goal_schema), 200

    def delete_goal(user_id):
        error = GoalService.delete_goal(user_id)
        if error:
            return {'msg': error}, 500
        return {'msg': "Excluído com sucesso"}, 200

    def add_exercise(user_id, data):
        exercise_register, error = validate_data(data, workout_schema)
        if error:
            return {'msg': error}, 400
        
        error, redundancy = GoalService.add_exercise(user_id, exercise_register)
        if error:
            return {'msg': error}, 500
        if redundancy:
            return {'msg': redundancy}, 400
        return {'msg': 'Adicionado com sucesso'}, 200

    def rmv_exercise(user_id, data):
        exercise_register, error = validate_data(data, workout_schema)
        if error:
            return {'msg': error}, 400
        
        error = GoalService.rmv_exercise(user_id, exercise_register)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Excluído com sucesso'}, 200

    def add_food(user_id, data):
        food_register, error = validate_data(data, diet_schema)
        if error:
            return {'msg': error}, 400
        
        error, redundancy = GoalService.add_food(user_id, food_register)
        if error:
            return {'msg': error}, 500
        if redundancy:
            return {'msg': redundancy}, 400
        return {'msg': 'Adicionado com sucesso'}, 200

    def rmv_food(user_id, data):
        food_register, error = validate_data(data, diet_schema)
        if error:
            return {'msg': error}, 400
        
        error = GoalService.rmv_food(user_id, food_register)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Excluído com sucesso'}, 200
