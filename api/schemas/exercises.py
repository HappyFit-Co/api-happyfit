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
    '_id': fields.String(required=False, description='Identificador único', example='6123456789abcdef01234567'),
    'name': fields.String(required=False, description='Nome', example='Exemplo de exercício'),
    'body_part': fields.String(required=False, description='Parte do corpo', example='Perna'),
    'target': fields.String(required=False, description='Músculo alvo', example='Quadríceps'),
    'repetition': fields.Integer(required=False, description='Número de repetições', example=10),
    'series': fields.Integer(required=False, description='Número de séries', example=3),
    'interval': fields.Integer(required=False, description='Tempo de intervalo entre séries', example=60),
    'equipment': fields.String(required=False, description='Equipamento', example='Barra de peso'),
    'description': fields.String(required=False, description='Descrição', example='Execute o exercício de forma lenta e contínua, sem interromper o movimento.'),
    'execution_gif': fields.String(required=False, description='Gif de execução do exercício', example='https://example.com/exercise.gif')
})

unauthorized_schema = ns.model('UnauthorizedResponse', {
    'msg': fields.String(required=False, description='Mensagem de não autorizado', example='Missing Authorization Header')
})

unprocessable_schema = ns.model('UnprocessableEntityResponse', {
    'msg': fields.String(required=False, description='Mensagem de entidade não processável', example='Bearer token from invalid header')
})

not_found_schema = ns.model('NotFoundResponse', {
    'msg': fields.String(required=False, description='Mensagem de não encontrado', example='Searched _id not found')
})

empty_list_schema = fields.List(fields.Raw, example=[])
