from flask_restx import marshal

from api.services.foods import FoodService
from api.schemas.foods import food_schema

class FoodController: 
    def get_all_foods():
        foods, error = FoodService.get_all_foods()
        if error:
            return {'msg': error}, 500
        if not foods:
            return [], 404
        return marshal(foods, food_schema), 200
    
    def get_food_by_id(food_id):
        food, error = FoodService.get_food_by_id(food_id)
        if error:
            return {'msg': error}, 500
        if not food:
            return {'msg': 'Nenhum dado encontrado'}, 404
        return marshal(food, food_schema), 200

    def get_food_by_name(food_name):
        foods, error = FoodService.get_food_by_name(food_name)
        if error:
            return {'msg': error}, 500
        if not foods:
            return [], 404
        return marshal(foods, food_schema), 200
    