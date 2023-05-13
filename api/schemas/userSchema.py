from flask_restx import fields, Namespace

from .goalSchema import goal_schema
from .historicSchema import historic_schema
from .notificationSchema import notification_schema

ns = Namespace('users', description='User operations')

user_schema = ns.model('User', {
    '_id': fields.String(),
    'name': fields.String(),
    'email': fields.String(),
    'pwd': fields.String(),
    'weight': fields.Float(),
    'height': fields.Float(),
    'age': fields.Integer(),
    'activity_level': fields.String(),
    'goal': fields.Nested(goal_schema),
    'historic': fields.Nested(historic_schema),
    'notification_config': fields.Nested(notification_schema),
})
