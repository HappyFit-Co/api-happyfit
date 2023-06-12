from flask_restx import Namespace, fields

from .foods import macro_schema

ns = Namespace('records', description='Operações relacionadas a registro')
  
# Analisar e validar os dados de entrada da solicitação HTTP e garantir que os campos obrigatórios estejam presentes   
workout_parser = ns.parser()
workout_parser.add_argument('exercise_id', type=str, required=True, help='Identificador único do exercício')
workout_parser.add_argument('hour', type=str, required=True, help='Hora do treino no formato HH:MM')

diet_parser = ns.parser()
diet_parser.add_argument('calories', type=int, required=True, help='Quantidade de calorias ingeridas')
diet_parser.add_argument('macro_nutrient', type=dict, required=True, help='Macro nutrientes ingeridos')
diet_parser.add_argument('hour', type=int, required=True, help='Hora da refeição no formato HH:MM')

create_record_parser = ns.parser()
create_record_parser.add_argument('daily_water', type=int, required=True, help='Quantidade de água ingerida no dia')
create_record_parser.add_argument('workout', type=list, required=True, location='json', help='Lista de treinos do dia')
create_record_parser.add_argument('diet', type=list, required=True, location='json', help='Lista de refeições do dia')

# Gerar a documentação automática do Swagger UI e a model
workout_schema = ns.model('RecordWorkout', {
    'exercise_id': fields.String(required=True, description='Identificador único do exercício', example='abcdef123456789012345645'),
    'hour': fields.String(required=True, description='Hora do treino no formato HH:MM', example='HH:MM')
})

diet_schema = ns.model('RecordDiet', {
    'food_record_id': fields.String(required=True, description='Identificador único do registro de dieta', example='abcdef123456789012345645'),
    'calories': fields.Integer(required=True, description='Quantidade de calorias ingeridas', example=100),
    'macro_nutrient': fields.Nested(macro_schema, required=True, description='Macro nutrientes ingeridos'),
    'hour': fields.String(required=True, description='Hora da refeição no formato HH:MM', example='HH:MM')
})

record_schema = ns.model('Record', {
    '_id': fields.String(required=True, description='Identificador único', example='6123456789abcdef01234567'),
    'date': fields.String(required=True, description='Data do registro no formato AAAA-MM-DD', example='AAAA-MM-DD'),
    'daily_calories': fields.Integer(required=True, description='Quantidade de calorias ingeridas no dia', example=100),
    'daily_water': fields.Integer(required=True, description='Quantidade de água ingerida no dia', example=2000),
    'daily_macro_nutrient': fields.Nested(macro_schema, required=True, description='Macro nutrientes ingeridos no dia'),
    'workout': fields.List(fields.Nested(workout_schema), required=True, description='Lista de exercícios realizados no dia'),
    'diet': fields.List(fields.Nested(diet_schema), required=True, description='Lista de alimentos consumidos no dia')
})

add_diet_schema = ns.model('RecordAddDiet', {
    'calories': fields.Integer(required=True, description='Quantidade de calorias ingeridas', example=100),
    'macro_nutrient': fields.Nested(macro_schema, required=True, description='Macro nutrientes ingeridos'),
    'hour': fields.String(required=True, description='Hora da refeição no formato HH:MM', example='HH:MM')
})

create_record_schema = ns.model('RecordCreate', {
    'daily_water': fields.Integer(required=True, description='Quantidade de água ingerida no dia', example=2000),
    'workout': fields.List(fields.Nested(workout_schema), required=True, description='Lista de exercícios realizados no dia'),
    'diet': fields.List(fields.Nested(add_diet_schema), required=True, description='Lista de alimentos consumidos no dia')
})

# Definindo valores padrão
default_record = {
    "daily_water": 0,
    "workout": [],
    "diet": []
}
