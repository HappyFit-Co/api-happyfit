from flask_restx import Namespace, fields

ns = Namespace('notifications', description='Operações relacionadas a notificações')

# Analisar e validar os dados de entrada da solicitação HTTP e garantir que os campos obrigatórios estejam presentes
notification_parser = ns.parser()
notification_parser.add_argument('workout', type=dict, required=True, help='Detalhes da notificação de treino')
notification_parser.add_argument('water', type=dict, required=True, help='Detalhes da notificação de água')

# Gerar a documentação automática do Swagger UI e a model
workout_schema = ns.model('Workout', {
    'frequency': fields.String(required=True, description='Frequência de treino'),
    'hour': fields.String(required=True, description='Horário do treino')
})

water_schema = ns.model('Water', {
    'frequency': fields.String(required=True, description='Frequência de hidratação'),
    'start_hour': fields.String(required=True, description='Horário de início da hidratação'),
    'end_hour': fields.String(required=True, description='Horário de término da hidratação')
})

notification_schema = ns.model('Notification', {
    'workout': fields.Nested(workout_schema, required=True, description='Detalhes da notificação de treino'),
    'water': fields.Nested(water_schema, required=True, description='Detalhes da notificação de água')
})
