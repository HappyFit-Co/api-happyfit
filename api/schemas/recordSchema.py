from flask_restx import Namespace, fields

from .foodSchema import macro_schema

ns = Namespace('records', description='Operações relacionadas a registro')
    
workout_schema = ns.model('Workout', {
    'exercise_id': fields.String(required=True, description='Identificador único do exercício'),
    'hour': fields.String(required=True, description='Hora do treino no formato HH:MM')
})

diet_schema = ns.model('Diet', {
    'calories': fields.Integer(required=True, description='Quantidade de calorias ingeridas'),
    'macro_nutrient': fields.Nested(macro_schema, required=True, description='Macro nutrientes ingeridos'),
    'hour': fields.String(required=True, description='Hora da refeição no formato HH:MM')
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
    '_id': fields.String(required=True, description='Identificador único'),
    'date': fields.String(required=True, description='Data do registro no formato AAAA-MM-DD'),
    'daily_calories': fields.Integer(required=True, description='Quantidade de calorias ingeridas no dia'),
    'daily_water': fields.Integer(required=True, description='Quantidade de água ingerida no dia'),
    'daily_macro_nutrient': fields.Nested(macro_schema, required=True, description='Macro nutrientes ingeridos no dia'),
    'workout': fields.List(fields.Nested(workout_schema), required=True, description='Lista de exercícios realizados no dia'),
    'diet': fields.List(fields.Nested(diet_schema), required=True, description='Lista de alimentos consumidos no dia')
})
