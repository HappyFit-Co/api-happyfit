from marshmallow import Schema, fields

from api.schemas.dietSchema import DietSchema, MacroSchema
from api.schemas.exerciseSchema import ExerciseSchema


class ConsumptionSchema(Schema):
    _id = fields.String()
    date = fields.Date()
    calories = fields.Integer()
    water = fields.Integer()
    macro_nutrient = fields.Nested(MacroSchema)
    exercise = fields.Nested(ExerciseSchema)
    diet = fields.Nested(DietSchema)