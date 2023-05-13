from flask_restx import fields, Namespace

from .foodSchema import macro_schema

ns = Namespace('record', description='Record operations')

workout_schema = ns.model('Workout', {
    'exercise_id': fields.String(required=True),
    'hour': fields.Time(required=True)
})

diet_schema = ns.model('Diet', {
    'calories': fields.Integer(required=True),
    'macro_nutrient': fields.Nested(macro_schema, required=True),
    'hour': fields.Time(required=True)
})

record_schema = ns.model('Record', {
    '_id': fields.String(required=True),
    'date': fields.Date(required=True),
    'daily_calories': fields.Integer(required=True),
    'daily_water': fields.Integer(required=True),
    'daily_macro_nutrient': fields.Nested(macro_schema, required=True),
    'workout': fields.List(fields.Nested(workout_schema)),
    'diet': fields.List(fields.Nested(diet_schema))
})
