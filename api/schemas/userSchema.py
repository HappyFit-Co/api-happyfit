from marshmallow import Schema, fields

from api.schemas.dietSchema import DietSchema, MacroSchema
from api.schemas.exerciseSchema import ExerciseSchema
from api.schemas.historicSchema import HistoricSchema


class GoalSchema(Schema):
    weight = fields.Float()
    objective = fields.String()
    calories = fields.Integer()
    water = fields.Integer()
    deadline = fields.Date()
    exercise = fields.Nested(ExerciseSchema)
    macro_nutrient = fields.Nested(MacroSchema)
    diet = fields.Nested(DietSchema)

class UserSchema(Schema):
    _id = fields.String()
    name = fields.String()
    email = fields.Email()
    pwd = fields.String()
    weight = fields.Float()
    height = fields.Float()
    age = fields.Integer()
    activity_level = fields.String()
    goal = fields.Nested(GoalSchema)
    historic = fields.Nested(HistoricSchema)