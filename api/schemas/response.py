from flask_restx import Namespace, fields

ns = Namespace('responses', description='Respostas em caso de não sucesso')

empty_list_schema = fields.List(fields.Raw, example=[])

unauthorized_schema = ns.model('UnauthorizedResponse', {
    'msg': fields.String(required=False, description='Mensagem de não autorizado', example='Missing Authorization Header')
})

unprocessable_schema = ns.model('UnprocessableEntityResponse', {
    'msg': fields.String(required=False, description='Mensagem de entidade não processável', example='Bearer token from invalid header')
})

not_found_schema = ns.model('NotFoundResponse', {
    'msg': fields.String(required=False, description='Mensagem de não encontrado', example='No data was found')
})

internal_server_schema = ns.model('InternalServerError', {
    'msg': fields.String(required=False, description='Mensagem de erro interno do servidoro', example='Error returning data from service')
})
