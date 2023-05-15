from api.services.foods import FoodService

class FoodController:
    def __init__(self):
        self.food_service = FoodService()

    def get_all_foods(self):
        foods = self.food_service.get_all_foods()
        if not foods:
            return foods, 404
        return foods, 200
    
    def get_food_by_id(self, food_id):
        food = self.food_service.get_food_by_id(food_id)
        if not food:
            return food, 404
        return food, 200

    def get_food_by_name(self, food_name):
        foods = self.food_service.get_food_by_name(food_name)
        if not foods:
            return foods, 404
        return foods, 200