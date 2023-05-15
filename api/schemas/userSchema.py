from flask_restx import Namespace, fields

from .goalSchema import goal_schema
from .historicSchema import historic_schema
from .notificationSchema import notification_schema

ns = Namespace('users', description='Operações relacionadas a usuários')

user_parser = ns.parser()
user_parser.add_argument('_id', type=str, required=True, help='Identificador único do usuário')
user_parser.add_argument('name', type=str, required=True, help='Nome do usuário')
user_parser.add_argument('email', type=str, required=True, help='Endereço de email do usuário')
user_parser.add_argument('pwd', type=str, required=True, help='Senha do usuário')
user_parser.add_argument('weight', type=float, required=True, help='Peso do usuário em kg')
user_parser.add_argument('height', type=float, required=True, help='Altura do usuário em metros')
user_parser.add_argument('age', type=int, required=True, help='Idade do usuário')
user_parser.add_argument('activity_level', type=str, required=True, help='Nível de atividade física do usuário')
user_parser.add_argument('goal', type=dict, required=True, help='Objetivo do usuário')
user_parser.add_argument('historic', type=dict, required=True, help='Histórico do usuário')
user_parser.add_argument('notification_config', type=dict, required=True, help='Configurações de notificação do usuário')

user_schema = ns.model('User', {
    '_id': fields.String(required=True, description='Identificador único do usuário'),
    'name': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='Endereço de email do usuário'),
    'pwd': fields.String(required=True, description='Senha do usuário'),
    'weight': fields.Float(required=True, description='Peso do usuário em kg'),
    'height': fields.Float(required=True, description='Altura do usuário em metros'),
    'age': fields.Integer(required=True, description='Idade do usuário'),
    'activity_level': fields.String(required=True, description='Nível de atividade física do usuário'),
    'goal': fields.Nested(goal_schema, required=True, description='Objetivo do usuário'),
    'historic': fields.Nested(historic_schema, required=True, description='Histórico do usuário'),
    'notification_config': fields.Nested(notification_schema, required=True, description='Configurações de notificação do usuário'),
})

