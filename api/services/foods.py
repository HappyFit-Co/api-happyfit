from api.utils.database import mongo
from bson.objectid import ObjectId 

class FoodService:
    def get_all_foods():
        try:
            foods = list(mongo.db.foods.find())
            return foods, None
        except:
            return None, 'Erro interno ao manipular dados no serviço'

    def get_food_by_id(food_id):
        try:
            food = mongo.db.foods.find_one({"_id": ObjectId(food_id)})
            return food, None
        except:
            return None, 'Erro interno ao manipular dados no serviço'

    def get_food_by_name(food_name):
        try:
            foods = list(mongo.db.foods.find({"name": {"$regex": food_name, "$options": "i"}}))
            return foods, None
        except:
            return None, 'Erro interno ao manipular dados no serviço'
