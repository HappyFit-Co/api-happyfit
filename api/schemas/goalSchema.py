from flask_restx import fields, Namespace, reqparse
from datetime import time, datetime

from .foodSchema import macro_schema

ns = Namespace('goal', description='Goal operations')

weekday_choices = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def validate_time(value):
    try:
        time.fromisoformat(value)
        return value
    except ValueError:
        raise ValueError("Invalid time format, use ISO format (HH:MM:SS)")

def validate_weekday(value):
    if value not in weekday_choices:
        raise ValueError("Invalid weekday, choose one of the following: " + ", ".join(weekday_choices))
    return value

def validate_date(value):
    try:
        datetime.strptime(value, '%Y-%m-%d').date()
        return value
    except ValueError:
        raise ValueError("Invalid date format, use ISO format (YYYY-MM-DD)")

workout_schema = ns.model('Workout', {
    'exercise_id': fields.String(required=True),
    'hour': fields.String(required=True, validate=validate_time),
    'weekday': fields.String(required=True, validate=validate_weekday)
})

diet_schema = ns.model('Diet', {
    'food_id': fields.String(required=True),
    'weekday': fields.String(required=True, validate=validate_weekday)
})

goal_parser = reqparse.RequestParser()
goal_parser.add_argument('weight', type=float, required=True)
goal_parser.add_argument('objective', type=str, required=True)
goal_parser.add_argument('daily_calories', type=int, required=True)
goal_parser.add_argument('daily_water', type=int, required=True)
goal_parser.add_argument('daily_macro_nutrient', type=dict, required=True)
goal_parser.add_argument('deadline', type=str, required=True, validate=validate_date)
goal_parser.add_argument('workout', type=list, location='json', items=fields.Nested(workout_schema))
goal_parser.add_argument('diet', type=list, location='json', items=fields.Nested(diet_schema))

goal_schema = ns.model('Goal', {
    'weight': fields.Float(required=True),
    'objective': fields.String(required=True),
    'daily_calories': fields.Integer(required=True),
    'daily_water': fields.Integer(required=True),
    'daily_macro_nutrient': fields.Nested(macro_schema, required=True),
    'deadline': fields.Date(required=True, validate=validate_date),
    'workout': fields.List(fields.Nested(workout_schema)),
    'diet': fields.List(fields.Nested(diet_schema))
})
