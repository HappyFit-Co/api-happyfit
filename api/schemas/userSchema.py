from dietSchema import DietSchema
from exerciseSchema import ExerciseSchema
from historicSchema import HistoricSchema
from marshmallow import Schema, fields


class GoalSchema(Schema):
    weight = fields.Float()
    objective = fields.String()
    calories = fields.Integer()
    macro_nutrient = fields.Dict(keys=fields.String(), values=fields.Integer())
    water = fields.Integer()
    deadline = fields.Date()
    exercise = fields.Nested(ExerciseSchema)
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