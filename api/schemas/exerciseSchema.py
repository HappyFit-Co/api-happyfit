from flask_restx import Namespace, fields

ns = Namespace('exercises', description='Operações relacionadas a exercícios')

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
