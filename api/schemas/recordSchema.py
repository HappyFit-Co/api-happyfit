from flask_restx import Namespace, fields
from datetime import time, datetime

from .foodSchema import macro_schema

ns = Namespace('records', description='Operações relacionadas a registro')

# Validação do horário do dia
def validate_time(value):
    try:
        time.fromisoformat(value)
        return value
    except ValueError:
        raise ValueError("Invalid time format, use ISO format (HH:MM:SS)")
    
# Validação de data
def validate_date(value):
    try:
        datetime.strptime(value, '%Y-%m-%d').date()
        return value
    except ValueError:
        raise ValueError("Invalid date format, use ISO format (YYYY-MM-DD)")
    
workout_schema = ns.model('Workout', {
    'exercise_id': fields.String(required=True, description='Identificador único do exercício'),
    'hour': fields.Time(required=True, validate=validate_time, description='Hora do treino no formato HH:MM')
})

diet_schema = ns.model('Diet', {
    'calories': fields.Integer(required=True, description='Quantidade de calorias ingeridas'),
    'macro_nutrient': fields.Nested(macro_schema, required=True, description='Macro nutrientes ingeridos'),
    'hour': fields.Time(required=True, validate=validate_time, description='Hora da refeição no formato HH:MM')
})
  
# Analisar e validar os dados de entrada da solicitação HTTP e garantir que os campos obrigatórios estejam presentes    
record_parser = ns.parser()
record_parser.add_argument('_id', type=str, required=True, help='Identificador único')
record_parser.add_argument('date', type=str, required=True, validate=validate_date, help='Data do registro no formato ISO (YYYY-MM-DD)'),
record_parser.add_argument('daily_calories', type=int, required=True, help='Calorias diárias')
record_parser.add_argument('daily_water', type=int, required=True, help='Quantidade de água ingerida no dia')
record_parser.add_argument('daily_macro_nutrient', type=dict, required=True, help='Macronutrientes diários')
record_parser.add_argument('workout', type=list, required=True, location='json', items=fields.Nested(workout_schema), help='Lista de treinos do dia')
record_parser.add_argument('diet', type=list, required=True, location='json', items=fields.Nested(diet_schema), help='Lista de refeições do dia')

# Gerar a documentação automática do Swagger UI e a model
record_schema = ns.model('Record', {
    '_id': fields.String(required=True, description='Identificador único'),
    'date': fields.Date(required=True, description='Data do registro no formato AAAA-MM-DD'),
    'daily_calories': fields.Integer(required=True, description='Quantidade de calorias ingeridas no dia'),
    'daily_water': fields.Integer(required=True, description='Quantidade de água ingerida no dia'),
    'daily_macro_nutrient': fields.Nested(macro_schema, required=True, description='Macro nutrientes ingeridos no dia'),
    'workout': fields.List(fields.Nested(workout_schema), required=True, description='Lista de exercícios realizados no dia'),
    'diet': fields.List(fields.Nested(diet_schema), required=True, description='Lista de alimentos consumidos no dia')
})
