from flask_restx import Api
from flask_pymongo import PyMongo

# Inicializa a extensão PyMongo
mongo = PyMongo()

# Cria o objeto Api, que é uma extensão do Flask
api = Api(
    version='1.0', 
    title='API RESTful - HappyFit', 
    description='''Este projeto consiste na construção de uma **API RESTful usando o framework Flask-RESTX** para criar um sistema que controle a ingestão de alimentos e água, além de gerenciar treinos de academia do usuário. Através de uma interface web, o aplicativo oferecerá notificações para incentivar hábitos saudáveis, como o consumo adequado de água e a definição de metas diárias. 
                    \n\nA API fornecerá aos usuários todas as funcionalidades necessárias para inserir e visualizar informações sobre **alimentação, hidratação e atividades físicas**. Além disso, ela será projetada para **garantir a segurança e a privacidade dos dados do usuário**, utilizando práticas de autenticação e autorização apropriadas.
                    \n\nO uso do Flask-RESTX permitirá uma fácil implementação dos endpoints da API, bem como a **geração automática da documentação do código**, tornando o processo de desenvolvimento mais eficiente e organizado.
                    \n\nEm suma, o objetivo deste software é **ajudar os usuários a adotar hábitos saudáveis**, monitorando suas atividades e oferecendo incentivos para manter uma rotina saudável. Através de uma API robusta construída com Flask-RESTX, esperamos fornecer uma solução completa e confiável para controle de alimentação, hidratação e atividades físicas.'''.strip(),
    license='MIT License',
    license_url='https://github.com/HappyFit-Co/api-happyfit/blob/main/LICENSE',
    authorizations={
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'X-API-Key',
            'description': 'Chave da API para autenticação de uso.'
        },
        'jwt': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Para autenticar, coloque o token JWT no formato **Bearer**.'
        }
    },
    security='jwt,apikey'
)

# Importa os namespaces criados
from api.routes.exercises import ns as exercise_namespace

# Adiciona os namespaces à API
api.add_namespace(exercise_namespace)

