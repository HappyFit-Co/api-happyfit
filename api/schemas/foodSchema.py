from marshmallow import Schema, fields


class FoodMacroSchema(Schema):
    protein = fields.Number()
    carbohydrate = fields.Number()
    fat = fields.Number()


class FoodSchema(Schema):
    _id = fields.String()
    name = fields.String()
    calories = fields.Integer()
    macro_nutrient = fields.Nested(FoodMacroSchema)
    portion = fields.Float()
    description = fields.String()