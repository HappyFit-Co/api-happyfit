from marshmallow import Schema, fields
from schemas import DietSchema, ExerciseSchema


class ConsumptionSchema(Schema):
    _id = fields.String()
    date = fields.Date()
    calories = fields.Integer()
    water = fields.Integer()
    macro_nutrient = fields.Dict(keys=fields.String(), values=fields.Integer())
    exercise = fields.Nested(ExerciseSchema)
    diet = fields.Nested(DietSchema)