from flask_restx import Resource
from api.controllers.foodController import FoodController
from api.schemas.foodSchema import ns, food_schema

food_controller = FoodController()