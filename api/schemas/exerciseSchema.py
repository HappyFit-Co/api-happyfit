from flask_restx import fields, Namespace

ns = Namespace('exercise', description='Exercise operations')

exercise_schema = ns.model('Exercise', {
    '_id': fields.String(),
    'name': fields.String(),
    'body_part': fields.String(),
    'target': fields.String(),
    'repetition': fields.Integer(),
    'series': fields.Integer(),
    'interval': fields.Integer(),
    'equipment': fields.String(),
    'execution_gif': fields.String()
})
