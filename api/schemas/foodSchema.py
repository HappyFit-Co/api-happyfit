from marshmallow import Schema, fields

class MacroSchema(Schema):
    protein = fields.Float()
    carbohydrate = fields.Float()
    fat = fields.Float()

class MineralSchema(Schema):
    sodium = fields.String()
    calcium = fields.String()
    magnesium = fields.String()
    potassium = fields.String()
    selenium = fields.String()
    zinc = fields.String()

class FoodSchema(Schema):
    _id = fields.String()
    name = fields.String()
    portion = fields.String()
    calories = fields.Integer()
    macro_nutrient = fields.Nested(MacroSchema)
    minerals = fields.Nested(MineralSchema)
    sugar = fields.String()
    fiber = fields.String()
