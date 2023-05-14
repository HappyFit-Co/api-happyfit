from flask_restx import Namespace, fields
from datetime import time, datetime

from .foodSchema import macro_schema

ns = Namespace('goals', description='Operações relacionadas a metas')

weekday_choices = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Validação do horário do dia
def validate_time(value):
    try:
        time.fromisoformat(value)
        return value
    except ValueError:
        raise ValueError("Invalid time format, use ISO format (HH:MM:SS)")

# Validação de dia da semana
def validate_weekday(value):
    if value not in weekday_choices:
        raise ValueError("Invalid weekday, choose one of the following: " + ", ".join(weekday_choices))
    return value

# Validação de data
def validate_date(value):
    try:
        datetime.strptime(value, '%Y-%m-%d').date()
        return value
    except ValueError:
        raise ValueError("Invalid date format, use ISO format (YYYY-MM-DD)")

workout_schema = ns.model('Workout', {
    'exercise_id': fields.String(required=True, description='Identificador único do exercício'),
    'hour': fields.String(required=True, validate=validate_time, description='Horário do dia'),
    'weekday': fields.String(required=True, validate=validate_weekday, description='Dia da Semana')
})

diet_schema = ns.model('Diet', {
    'food_id': fields.String(required=True, description='Identificador único do alimento'),
    'weekday': fields.String(required=True, validate=validate_weekday, description='Dia da Semana')
})

# Analisar e validar os dados de entrada da solicitação HTTP e garantir que os campos obrigatórios estejam presentes
goal_parser = ns.parser()
goal_parser.add_argument('weight', type=float, required=True, help='Peso do usuário em kg')
goal_parser.add_argument('objective', type=str, required=True, help='Objetivo do usuário')
goal_parser.add_argument('daily_calories', type=int, required=True, help='Calorias diárias recomendadas para o usuário')
goal_parser.add_argument('daily_water', type=int, required=True, help='Quantidade de água diária recomendada para o usuário')
goal_parser.add_argument('daily_macro_nutrient', type=dict, required=True, help='Macronutrientes diários recomendados para o usuário')
goal_parser.add_argument('deadline', type=str, required=True, validate=validate_date, help='Prazo para alcançar a meta no formato ISO (YYYY-MM-DD)'),
goal_parser.add_argument('workout', type=list, required=True, location='json', items=fields.Nested(workout_schema), help='Lista de treinos diários do usuário')
goal_parser.add_argument('diet', type=list, required=True, location='json', items=fields.Nested(diet_schema), help='Lista de refeições diárias do usuário')

# Gerar a documentação automática do Swagger UI e a model
goal_schema = ns.model('Goal', {
    'weight': fields.Float(required=True, description='Peso do usuário'),
    'objective': fields.String(required=True, description='Objetivo do usuário'),
    'daily_calories': fields.Integer(required=True, description='Calorias diárias do usuário'),
    'daily_water': fields.Integer(required=True, description='Água diária que o usuário deve ingerir'),
    'daily_macro_nutrient': fields.Nested(macro_schema, required=True, description='Macronutrientes diários do usuário'),
    'deadline': fields.Date(required=True, validate=validate_date, description='Prazo para alcançar a meta'),
    'workout': fields.List(fields.Nested(workout_schema), required=True, description='Treinos diários do usuário'),
    'diet': fields.List(fields.Nested(diet_schema), required=True, description='Alimentação diária do usuário')
})
