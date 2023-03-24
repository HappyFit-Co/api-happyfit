from marshmallow import Schema, fields

from api.schemas.exerciseSchema import ExerciseSchema
from api.schemas.foodSchema import FoodMacroSchema, FoodSchema
from api.schemas.historicSchema import HistoricSchema


class UserGoalSchema(Schema):
    weight = fields.Float(required=True)
    objective = fields.String(required=True)
    caloriesDay = fields.Integer(required=True)
    macro_nutrientDay = fields.Nested(FoodMacroSchema, required=True)
    waterDay = fields.Integer(required=True)
    deadline = fields.Date(required=True)
    workout = fields.String(many=True, required=True)
    diet = fields.String(many=True, required=True)


class UserSchema(Schema):
    _id = fields.String()
    name = fields.String(required=True)
    email = fields.Email(required=True)
    pwd = fields.String(required=True)
    weight = fields.Float()
    height = fields.Float()
    age = fields.Integer()
    activity_level = fields.String()
    goal = fields.Nested(UserGoalSchema, required=True)
    historic = fields.Nested(HistoricSchema, required=True)
