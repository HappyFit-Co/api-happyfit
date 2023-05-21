from flask_restx import Namespace, fields

ns = Namespace('responses', description='Respostas em caso de não sucesso')

update_sucess_schema = ns.model('UpdateSucessResponse', {
    'msg': fields.String(required=False, description='Mensagem de sucesso na edição de dados', example='Successfully updated')
})

delete_sucess_schema = ns.model('DeleteSucessResponse', {
    'msg': fields.String(required=False, description='Mensagem de sucesso na exclusão de dados', example='Successfully deleted')
})

login_sucess_schema = ns.model('LoginSucessResponse', {
    'access_token': fields.String(required=False, description='Mensagem de sucesso ao fazer login', example='<token>')
})

empty_list_schema = fields.List(fields.Raw, example=[])

unauthorized_schema = ns.model('UnauthorizedResponse', {
    'msg': fields.String(required=False, description='Mensagem de não autorizado', example='Missing Authorization Header')
})

invalid_credentials_schema = ns.model('InvalidCredentialsResponse', {
    'msg': fields.String(required=False, description='Mensagem de credenciais inválidas', example='Invalid user credentials')
})

bad_request_schema = ns.model('BadRequestResponse', {
    'msg': fields.String(required=False, description='Mensagem de requisição inválida', example='Invalid or incomplete input data')
})

unprocessable_schema = ns.model('UnprocessableEntityResponse', {
    'msg': fields.String(required=False, description='Mensagem de entidade não processável', example='Bearer token from invalid header')
})

not_found_schema = ns.model('NotFoundResponse', {
    'msg': fields.String(required=False, description='Mensagem de não encontrado', example='No data was found')
})

internal_server_schema = ns.model('InternalServerError', {
    'msg': fields.String(required=False, description='Mensagem de erro interno do servidoro', example='Internal error handling data in service')
})
