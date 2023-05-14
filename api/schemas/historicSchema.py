from flask_restx import Namespace, fields

from .recordSchema import record_schema

ns = Namespace('historics', description='Operações relacionadas ao histórico')

# Analisar e validar os dados de entrada da solicitação HTTP e garantir que os campos obrigatórios estejam presentes
historic_parser = ns.parser()
historic_parser.add_argument('historic', type=list, required=True, location='json', items=fields.Nested(record_schema), help='Registro de histórico do usuário')

# Gerar a documentação automática do Swagger UI e a model
historic = ns.model('Historic', {
    'historic': fields.List(fields.Nested(record_schema, required=True, description='Registro de histórico')),
})
