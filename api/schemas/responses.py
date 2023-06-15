from flask_restx import Namespace, fields

ns = Namespace('responses', description='Mensagens de Payload')

add_sucess_schema = ns.model('ResponseAddSucess', {
    'msg': fields.String(required=False, description='Mensagem de sucesso na adição de dados', example='Adicionado com sucesso')
})

update_sucess_schema = ns.model('ResponseUpdateSucess', {
    'msg': fields.String(required=False, description='Mensagem de sucesso na edição de dados', example='Atualizado com sucesso')
})

delete_sucess_schema = ns.model('ResponseDeleteSucess', {
    'msg': fields.String(required=False, description='Mensagem de sucesso na exclusão de dados', example='Excluído com sucesso')
})

login_sucess_schema = ns.model('ResponseLoginSucess', {
    'access_token': fields.String(required=False, description='Mensagem de sucesso ao fazer login', example='<token>')
})

empty_list_schema = fields.List(fields.Raw, example=[])

unauthorized_schema = ns.model('ResponseUnauthorized', {
    'msg': fields.String(required=False, description='Mensagem de não autorizado', example='Missing Authorization Header')
})

invalid_credentials_schema = ns.model('ResponseInvalidCredentials', {
    'msg': fields.String(required=False, description='Mensagem de credenciais inválidas', example='Credenciais de usuário inválidas')
})

bad_request_schema = ns.model('ResponseBadRequest', {
    'msg': fields.String(required=False, description='Mensagem de requisição inválida', example='Dados de entrada inválidos ou incompletos')
})

redundancy_schema = ns.model('ResponseRedundancy', {
    'msg': fields.String(required=False, description='Mensagem de redundância de dados', example='Os dados já existem, evite redundância')
})

not_found_schema = ns.model('ResponseNotFound', {
    'msg': fields.String(required=False, description='Mensagem de não encontrado', example='Nenhum dado encontrado')
})

unprocessable_schema = ns.model('ResponseUnprocessableEntity', {
    'msg': fields.String(required=False, description='Mensagem de entidade não processável', example='Bearer token from invalid header')
})

internal_server_schema = ns.model('ResponseInternalServerError', {
    'msg': fields.String(required=False, description='Mensagem de erro interno do servidoro', example='Erro interno ao manipular dados no serviço')
})
