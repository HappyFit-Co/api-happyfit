from marshmallow import Schema, fields, validate
from api.schemas.foodSchema import MacroSchema

class WorkoutSchema(Schema):
    exercise_id = fields.String()
    hour = fields.Time()
    weekday = fields.String(validate=validate.OneOf(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']))  

class DietSchema(Schema):
    food_id = fields.String()
    weekday = fields.String(validate=validate.OneOf(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']))  

class GoalSchema(Schema):
    weight = fields.Float()
    objective = fields.String()
    daily_calories = fields.Integer()
    daily_water = fields.Integer()
    daily_macro_nutrient = fields.Nested(MacroSchema)
    deadline = fields.Date()
    workout = fields.Nested(WorkoutSchema, many=True)
    diet = fields.Nested(DietSchema, many=True)