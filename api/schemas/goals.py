from flask_restx import Namespace, fields

from .foods import macro_schema

ns = Namespace('goals', description='Operações relacionadas a metas')

workout_schema = ns.model('GoalWorkout', {
    'exercise_id': fields.String(required=True, description='Identificador único do exercício', example='abcdef123456789012345645'),
    'hour': fields.String(required=True, description='Horário do dia', example='HH:MM'),
    'weekday': fields.String(required=True, description='Dia da Semana', example='domingo')
})

diet_schema = ns.model('GoalDiet', {
    'food_id': fields.String(required=True, description='Identificador único do alimento', example='abcdef123456789012345645'),
    'weekday': fields.String(required=True, description='Dia da Semana', example='domingo')
})

# Analisar e validar os dados de entrada da solicitação HTTP e garantir que os campos obrigatórios estejam presentes
goal_parser = ns.parser()
goal_parser.add_argument('weight', type=float, required=True, help='Peso do usuário em kg')
goal_parser.add_argument('objective', type=str, required=True, help='Objetivo do usuário')
goal_parser.add_argument('daily_calories', type=int, required=True, help='Calorias diárias recomendadas para o usuário')
goal_parser.add_argument('daily_water', type=int, required=True, help='Quantidade de água diária recomendada para o usuário')
goal_parser.add_argument('daily_macro_nutrient', type=dict, required=True, help='Macronutrientes diários recomendados para o usuário')
goal_parser.add_argument('deadline', type=str, required=True, help='Prazo para alcançar a meta no formato ISO (YYYY-MM-DD)'),
goal_parser.add_argument('workout', type=list, required=True, location='json', help='Lista de treinos diários do usuário')
goal_parser.add_argument('diet', type=list, required=True, location='json', help='Lista de refeições diárias do usuário')

# Gerar a documentação automática do Swagger UI e a model
goal_schema = ns.model('Goal', {
    'weight': fields.Float(required=True, description='Peso do usuário', example=78),
    'objective': fields.String(required=True, description='Objetivo do usuário', example="Emagrecer"),
    'daily_calories': fields.Integer(required=True, description='Calorias diárias do usuário', example=2500),
    'daily_water': fields.Integer(required=True, description='Água diária que o usuário deve ingerir', example=3000),
    'daily_macro_nutrient': fields.Nested(macro_schema, required=True, description='Macronutrientes diários do usuário'),
    'deadline': fields.String(required=True, description='Prazo para alcançar a meta', example='AAAA-MM-DD'),
    'workout': fields.List(fields.Nested(workout_schema), required=True, description='Treinos diários do usuário'),
    'diet': fields.List(fields.Nested(diet_schema), required=True, description='Alimentação diária do usuário')
})

# Definindo valores padrão
default_goal = {
    "weight": 0,
    "objective": "",
    "daily_calories": 0,
    "daily_water": 0,
    "daily_macro_nutrient": {
        "protein": 0,
        "carbohydrate": 0,
        "fat": 0
    },
    "deadline": "",
    "workout": [],
    "diet": []
}