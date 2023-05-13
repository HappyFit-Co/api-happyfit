from flask_restx import fields, Namespace

ns = Namespace('food', description='Food operations')

macro_schema = ns.model('Macro', {
    'protein': fields.Float(),
    'carbohydrate': fields.Float(),
    'fat': fields.Float()
})

mineral_schema = ns.model('Mineral', {
    'sodium': fields.String(),
    'calcium': fields.String(),
    'magnesium': fields.String(),
    'potassium': fields.String(),
    'selenium': fields.String(),
    'zinc': fields.String()
})

food_schema = ns.model('Food', {
    '_id': fields.String(),
    'name': fields.String(),
    'portion': fields.String(),
    'calories': fields.Integer(),
    'macro_nutrient': fields.Nested(macro_schema),
    'minerals': fields.Nested(mineral_schema),
    'sugar': fields.String(),
    'fiber': fields.String()
})
