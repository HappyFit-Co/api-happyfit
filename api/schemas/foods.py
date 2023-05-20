from flask_restx import Namespace, fields 

ns = Namespace('foods', description='Operações relacionadas a comidas')

# Analisar e validar os dados de entrada da solicitação HTTP e garantir que os campos obrigatórios estejam presentes
food_parser = ns.parser()
food_parser.add_argument('_id', type=str, required=True, help='Identificador único')
food_parser.add_argument('name', type=str, required=True, help='Nome da comida')
food_parser.add_argument('portion', type=str, required=True, help='Porção da comida')
food_parser.add_argument('calories', type=int, required=True, help='Quantidade de calorias')
food_parser.add_argument('macro_nutrient', type=dict, required=True, help='Macro nutrientes (proteína, carboidrato e gordura)')
food_parser.add_argument('minerals', type=dict, required=True, help='Minerais (sódio, cálcio, magnésio, potássio, selênio e zinco)')
food_parser.add_argument('sugar', type=str, required=True, help='Quantidade de açúcar')
food_parser.add_argument('fiber', type=str, required=True, help='Quantidade de fibras')

# Gerar a documentação automática do Swagger UI e a model
macro_schema = ns.model('FoodMacro', {
    'protein': fields.Float(required=True, description='Quantidade de proteínas', example=20),
    'carbohydrate': fields.Float(required=True, description='Quantidade de carboidratos', example=50),
    'fat': fields.Float(required=True, description='Quantidade de gorduras', example=5)
})

mineral_schema = ns.model('FoodMineral', {
    'sodium': fields.String(required=True, description='Quantidade de sódio'),
    'calcium': fields.String(required=True, description='Quantidade de cálcio'),
    'magnesium': fields.String(required=True, description='Quantidade de magnésio'),
    'potassium': fields.String(required=True, description='Quantidade de potássio'),
    'selenium': fields.String(required=True, description='Quantidade de selênio'),
    'zinc': fields.String(required=True, description='Quantidade de zinco')
})

food_schema = ns.model('Food', {
    '_id': fields.String(description='Identificador único'),
    'name': fields.String(required=True, description='Nome da comida'),
    'portion': fields.String(required=True, description='Porção da comida'),
    'calories': fields.Integer(required=True, description='Quantidade de calorias'),
    'macro_nutrient': fields.Nested(macro_schema, required=True, description='Macro nutrientes (proteína, carboidrato e gordura)'),
    'minerals': fields.Nested(mineral_schema, required=True, description='Minerais (sódio, cálcio, magnésio, potássio, selênio e zinco)'),
    'sugar': fields.String(description='Quantidade de açúcar'),
    'fiber': fields.String(description='Quantidade de fibras')
})
