from marshmallow import Schema, fields


class MacroSchema(Schema):
    protein = fields.Number()
    carbohydrate = fields.Number()
    fat = fields.Number()

class DietSchema(Schema):
    _id = fields.String()
    name = fields.String()
    calories = fields.Integer()
    macro_nutrient = fields.Nested(MacroSchema)
    portion = fields.Float()
    description = fields.String()