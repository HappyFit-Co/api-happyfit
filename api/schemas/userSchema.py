from marshmallow import Schema, fields
from api.schemas.goalSchema import GoalSchema
from api.schemas.historicSchema import HistoricSchema

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