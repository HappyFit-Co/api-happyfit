from flask_restx import Namespace, fields

from .goals import goal_schema
from .notifications import notification_schema
from .records import record_schema

ns = Namespace('users', description='Operações relacionadas a usuários')

user_parser = ns.parser()
user_parser.add_argument('_id', type=str, required=True, help='Identificador único do usuário')
user_parser.add_argument('name', type=str, required=True, help='Nome do usuário')
user_parser.add_argument('email', type=str, required=True, help='Endereço de email do usuário')
user_parser.add_argument('pwd', type=str, required=True, help='Senha do usuário')
user_parser.add_argument('weight', type=float, required=True, help='Peso do usuário em kg')
user_parser.add_argument('height', type=float, required=True, help='Altura do usuário em metros')
user_parser.add_argument('birthday', type=str, required=True, help='Data de Nascimento no formato AAAA-MM-DD')
user_parser.add_argument('sex', type=str, required=True, help='Sexo biológico')
user_parser.add_argument('activity_level', type=str, required=True, help='Nível de atividade física do usuário')
user_parser.add_argument('goal', type=dict, required=True, help='Objetivo do usuário')
user_parser.add_argument('historic', type=dict, required=True, help='Histórico do usuário')
user_parser.add_argument('notification_config', type=dict, required=True, help='Configurações de notificação do usuário')

user_schema = ns.model('User', {
    '_id': fields.String(required=True, description='Identificador único do usuário', example='6123456789abcdef01234567'),
    'name': fields.String(required=True, description='Nome do usuário', example='Nome do usuário'),
    'email': fields.String(required=True, description='Endereço de email do usuário', example='nome@example.com'),
    'pwd': fields.String(required=True, description='Senha do usuário', example='<senha com hash>'),
    'weight': fields.Float(required=True, description='Peso do usuário em kg', example=80),
    'height': fields.Float(required=True, description='Altura do usuário em metros', example=1.8),
    'birthday': fields.String(required=True, description='Data de Nascimento no formato AAAA-MM-DD', example='AAAA-MM-DD'),
    'sex': fields.String(required=True, description='Sexo biológico', example='Masculino'),
    'activity_level': fields.String(required=True, description='Nível de atividade física do usuário', example='Moderate'),
    'goal': fields.Nested(goal_schema, required=True, description='Objetivo do usuário'),
    'historic': fields.List(fields.Nested(record_schema, required=True, description='Registro de histórico')),
    'notification_config': fields.Nested(notification_schema, required=True, description='Configurações de notificação do usuário'),
})

create_user_schema = ns.model('UserCreate', {
    'name': fields.String(required=True, description='Nome do usuário', example='Nome do usuário'),
    'email': fields.String(required=True, description='Endereço de email do usuário', example='nome@example.com'),
    'pwd': fields.String(required=True, description='Senha do usuário', example='<senha sem hash>'),
    'weight': fields.Float(required=True, description='Peso do usuário em kg', example=80),
    'height': fields.Float(required=True, description='Altura do usuário em metros', example=1.8),
    'birthday': fields.String(required=True, description='Data de Nascimento no formato AAAA-MM-DD', example='AAAA-MM-DD'),
    'sex': fields.String(required=True, description='Sexo biológico', example='Masculino'),
    'activity_level': fields.String(required=True, description='Nível de atividade física do usuário', example='Moderate')
})

login_user_schema = ns.model('UserLogin', {
    'email': fields.String(required=True, description='Endereço de email do usuário', example='nome@example.com'),
    'pwd': fields.String(required=True, description='Senha do usuário', example='<senha sem hash>')
})
