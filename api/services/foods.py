from api.utils.database import mongo
from bson.objectid import ObjectId

class FoodService:
    def get_all_foods(self):
        foods = list(mongo.db.foods.find())
        return foods

    def get_food_by_id(self, food_id):
        food = mongo.db.foods.find_one({"_id": ObjectId(food_id)})
        return food

    def get_food_by_name(self, food_name):
        foods = list(mongo.db.foods.find({"name": {"$regex": food_name, "$options": "i"}}))
        return foods
