from marshmallow import Schema, fields

from api.schemas.exerciseSchema import ExerciseSchema
from api.schemas.foodSchema import FoodMacroSchema, FoodSchema


class ConsumptionSchema(Schema):
    _id = fields.String()
    date = fields.Date()
    calories = fields.Integer()
    water = fields.Integer()
    macro_nutrient = fields.Nested(FoodMacroSchema)
    workout = fields.Nested(ExerciseSchema, many=True)
    diet = fields.Nested(FoodSchema, many=True)