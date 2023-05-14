from flask_restx import Namespace, fields
from datetime import time

ns = Namespace('notifications', description='Operações relacionadas a notificações')

workout_frequency = ['daily', 'weekly', 'every other day', 'every weekday', 'every weekend']
water_frequency = ['hourly', 'every 2 hours', 'every 3 hours', 'every 4 hours', 'every 6 hours']

# Validação do horário do dia
def validate_time(value):
    try:
        time.fromisoformat(value)
        return value
    except ValueError:
        raise ValueError("Invalid time format, use ISO format (HH:MM:SS)")

# Analisar e validar os dados de entrada da solicitação HTTP e garantir que os campos obrigatórios estejam presentes
notification_parser = ns.parser()
notification_parser.add_argument('workout', type=dict, required=True, help='Detalhes da notificação de treino')
notification_parser.add_argument('water', type=dict, required=True, help='Detalhes da notificação de água')

# Gerar a documentação automática do Swagger UI e a model
workout = ns.model('Workout', {
    'frequency': fields.String(required=True, validate=fields.validate.OneOf(workout_frequency), description='Frequência de treino'),
    'hour': fields.String(required=True, validate=validate_time, description='Horário do treino')
})

water = ns.model('Water', {
    'frequency': fields.String(required=True, validate=fields.validate.OneOf(water_frequency), description='Frequência de hidratação'),
    'start_hour': fields.String(required=True, validate=validate_time, description='Horário de início da hidratação'),
    'end_hour': fields.String(required=True, validate=validate_time, description='Horário de término da hidratação')
})

notification_schema = ns.model('Notification', {
    'workout': fields.Nested(workout, required=True, description='Detalhes da notificação de treino'),
    'water': fields.Nested(water, required=True, description='Detalhes da notificação de água')
})
