from flask_restx import Namespace, fields

ns = Namespace('exercises', description='Operações relacionadas a exercícios')

# Analisar e validar os dados de entrada da solicitação HTTP e garantir que os campos obrigatórios estejam presentes
exercise_parser = ns.parser()
exercise_parser.add_argument('_id', type=str, required=True, help='Identificador único')
exercise_parser.add_argument('name', type=str, required=True, help='Nome')
exercise_parser.add_argument('body_part', type=str, required=True, help='Parte do corpo')
exercise_parser.add_argument('target', type=str, required=True, help='Músculo alvo')
exercise_parser.add_argument('repetition', type=int, required=True, help='Número de repetições')
exercise_parser.add_argument('series', type=int, required=True, help='Número de séries')
exercise_parser.add_argument('interval', type=int, required=True, help='Tempo de intervalo entre séries')
exercise_parser.add_argument('equipment', type=str, required=True, help='Equipamento')
exercise_parser.add_argument('execution_gif', type=str, required=True, help='Gif de execução do exercício')

# Gerar a documentação automática do Swagger UI e a model
exercise_schema = ns.model('Exercise', {
    '_id': fields.String(required=True, description='Identificador único'),
    'name': fields.String(required=True, description='Nome'),
    'body_part': fields.String(required=True, description='Parte do corpo'),
    'target': fields.String(required=True, description='Músculo alvo'),
    'repetition': fields.Integer(required=True, description='Número de repetições'),
    'series': fields.Integer(required=True, description='Número de séries'),
    'interval': fields.Integer(required=True, description='Tempo de intervalo entre séries'),
    'equipment': fields.String(required=True, description='Equipamento'),
    'execution_gif': fields.String(required=True, description='Gif de execução do exercício')
})

