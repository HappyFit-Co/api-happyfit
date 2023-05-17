from flask_restx import Namespace, fields

from .foods import macro_schema

ns = Namespace('records', description='Operações relacionadas a registro')
    
workout_schema = ns.model('Workout', {
    'exercise_id': fields.String(required=True, description='Identificador único do exercício', example='abcdef123456789012345645'),
    'hour': fields.String(required=True, description='Hora do treino no formato HH:MM', example='HH:MM')
})

diet_schema = ns.model('Diet', {
    'calories': fields.Integer(required=True, description='Quantidade de calorias ingeridas', example=100),
    'macro_nutrient': fields.Nested(macro_schema, required=True, description='Macro nutrientes ingeridos'),
    'hour': fields.String(required=True, description='Hora da refeição no formato HH:MM', example='HH:MM')
})
  
# Analisar e validar os dados de entrada da solicitação HTTP e garantir que os campos obrigatórios estejam presentes    
record_parser = ns.parser()
record_parser.add_argument('_id', type=str, required=True, help='Identificador único')
record_parser.add_argument('date', type=str, required=True, help='Data do registro no formato ISO (YYYY-MM-DD)'),
record_parser.add_argument('daily_calories', type=int, required=True, help='Calorias diárias')
record_parser.add_argument('daily_water', type=int, required=True, help='Quantidade de água ingerida no dia')
record_parser.add_argument('daily_macro_nutrient', type=dict, required=True, help='Macronutrientes diários')
record_parser.add_argument('workout', type=list, required=True, location='json', help='Lista de treinos do dia')
record_parser.add_argument('diet', type=list, required=True, location='json', help='Lista de refeições do dia')

# Gerar a documentação automática do Swagger UI e a model
record_schema = ns.model('Record', {
    '_id': fields.String(required=True, description='Identificador único', example='6123456789abcdef01234567'),
    'date': fields.String(required=True, description='Data do registro no formato AAAA-MM-DD', example='AAAA-MM-DD'),
    'daily_calories': fields.Integer(required=True, description='Quantidade de calorias ingeridas no dia', example=100),
    'daily_water': fields.Integer(required=True, description='Quantidade de água ingerida no dia', example=2000),
    'daily_macro_nutrient': fields.Nested(macro_schema, required=True, description='Macro nutrientes ingeridos no dia'),
    'workout': fields.List(fields.Nested(workout_schema), required=True, description='Lista de exercícios realizados no dia'),
    'diet': fields.List(fields.Nested(diet_schema), required=True, description='Lista de alimentos consumidos no dia')
})

create_record_schema = ns.model('CreateRecord', {
    'daily_water': fields.Integer(required=True, description='Quantidade de água ingerida no dia', example=2000),
    'workout': fields.List(fields.Nested(workout_schema), required=True, description='Lista de exercícios realizados no dia'),
    'diet': fields.List(fields.Nested(diet_schema), required=True, description='Lista de alimentos consumidos no dia')
})

unauthorized_schema = ns.model('UnauthorizedResponse', {
    'msg': fields.String(required=False, description='Mensagem de não autorizado', example='Missing Authorization Header')
})

unprocessable_schema = ns.model('UnprocessableEntityResponse', {
    'msg': fields.String(required=False, description='Mensagem de entidade não processável', example='Bearer token from invalid header')
})

not_found_schema = ns.model('NotFoundResponse', {
    'msg': fields.String(required=False, description='Mensagem de não encontrado', example='Requested resource not found')
})

bad_request_schema = ns.model('BadRequestResponse', {
    'msg': fields.String(required=False, description='Mensagem de requisição inválida', example='Invalid request due to errors or inappropriate customer data')
})
