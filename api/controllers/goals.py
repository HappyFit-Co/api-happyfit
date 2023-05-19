from flask_restx import marshal

from api.schemas.goals import goal_schema
from api.services.goals import GoalService
from api.utils.validate import (validate_day_of_week, validate_exercise_goal,
                                validate_food_goal, validate_hour_format,
                                validate_macro_schema)


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
        # Pré validação
        error = validate_macro_schema(data["daily_macro_nutrient"])
        if error:
            return {"msg": error}

        response = GoalService.edit_goal(user_id, data)

        # Tratamento de errros
        if isinstance(response, tuple):
            return response

        if not response:
            return {}, 404

        return marshal(response, goal_schema), 200

    def put_goal(user_id, data):
        # Pré validação
        error = validate_macro_schema(data["daily_macro_nutrient"])
        if error:
            return {"msg": error}

        response = GoalService.edit_goal(user_id, data)

        # Tratamento de errros
        if isinstance(response, tuple):
            return response

        if not response:
            return {}, 404
        return marshal(response, goal_schema), 200

    def delete_goal(user_id):
        return GoalService.delete_goal(user_id)

    def add_exercise(user_id, exercise_register):
        error = validate_exercise_goal(exercise_register)
        if error:
            return {"msg": error}

        return GoalService.add_exercise(user_id, exercise_register)

    def rmv_exercise(user_id, exercise_register):
        error = validate_exercise_goal(exercise_register)
        if error:
            return {"msg": error}

        return GoalService.rmv_exercise(user_id, exercise_register)

    def add_food(user_id, food_register):
        error = validate_food_goal(food_register)
        if error:
            return {"msg": error}

        return GoalService.add_food(user_id, food_register)

    def rmv_food(user_id, food_register):
        error = validate_food_goal(food_register)
        if error:
            return {"msg": error}
        
        return GoalService.rmv_food(user_id, food_register)
