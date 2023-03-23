from marshmallow import Schema, fields


class DietSchema(Schema):
    _id = fields.String()
    name = fields.String()
    calories = fields.Integer()
    macro_nutrient = fields.Dict(keys=fields.String(), values=fields.Integer())
    portion = fields.Float()
    description = fields.String()