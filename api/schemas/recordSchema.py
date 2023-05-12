from marshmallow import Schema, fields
from api.schemas.foodSchema import MacroSchema

class WorkoutSchema(Schema):
    exercise_id = fields.String()
    hour = fields.Time()

class DietSchema(Schema):
    calories = fields.Integer()
    macro_nutrient = fields.Nested(MacroSchema)
    hour = fields.Time()

class RecordSchema(Schema):
    _id = fields.String()
    date = fields.Date()
    daily_calories = fields.Integer()
    daily_water = fields.Integer()
    daily_macro_nutrient = fields.Nested(MacroSchema)
    workout = fields.Nested(WorkoutSchema, many=True)
    diet = fields.Nested(DietSchema, many=True)