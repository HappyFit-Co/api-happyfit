from flask_restx import fields, Namespace

from .recordSchema import record_schema

ns = Namespace('historic', description='Historic operations')

historic = ns.model('Historic', {
    'historic': fields.List(fields.Nested(record_schema), required=True)
})
