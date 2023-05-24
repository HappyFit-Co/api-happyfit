from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource

from api.controllers.goals import GoalController
from api.schemas.goals import (
    ns,
    goal_schema,
    workout_schema,
    diet_schema
    )
from api.schemas.response import (
    add_sucess_schema,
    update_sucess_schema,
    delete_sucess_schema,
    bad_request_schema,
    redundancy_schema,
    unauthorized_schema,
    not_found_schema,
    unprocessable_schema,
    internal_server_schema
)

@ns.route('/')
class Goal(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna a meta do usuário')
    @ns.response(200, 'Sucesso', goal_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self):
        """Vizualiza a meta do usuário"""
        return GoalController.get_goal(get_jwt_identity())

    @jwt_required()
    @ns.doc(security='jwt', description='Gerencia a meta do usuário')
    @ns.expect(goal_schema)
    @ns.response(201, 'Criado', goal_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def post(self):
        """Cria a meta do usuário"""
        return GoalController.post_goal(get_jwt_identity(), ns.payload)
        
    @jwt_required()
    @ns.doc(security='jwt', description='Edita a meta do usuário')
    @ns.expect(goal_schema)
    @ns.response(200, 'Sucesso', update_sucess_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def put(self):
        """Edita a meta do usuário"""
        return GoalController.put_goal(get_jwt_identity(), ns.payload)

    @jwt_required()
    @ns.doc(security='jwt', description='Deleta a meta do usuário')
    @ns.response(200, 'Sucesso', delete_sucess_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def delete(self):
        """Deleta a meta do usuário"""
        return GoalController.delete_goal(get_jwt_identity())

@ns.route('/workout/add')
class AddExercise(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Adiciona exercício à meta do usuário')
    @ns.expect(workout_schema)
    @ns.response(201, 'Criado', add_sucess_schema)
    @ns.response(400, 'Redundância de dados', redundancy_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def put(self):
        """Adiciona exercício à meta do usuário"""
        return GoalController.add_exercise(get_jwt_identity(), ns.payload)

@ns.route('/workout/remove')
class RemoveExercise(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Deleta exercício da meta do usuário')
    @ns.expect(workout_schema)
    @ns.response(200, 'Sucesso', delete_sucess_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def put(self):
        """Deleta exercício da meta do usuário"""
        return GoalController.rmv_exercise(get_jwt_identity(), ns.payload)

@ns.route('/diet/add')
class AddDiet(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Adiciona comida à meta do usuário')
    @ns.expect(diet_schema)
    @ns.response(201, 'Criado', add_sucess_schema)
    @ns.response(400, 'Redundância de dados', redundancy_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def put(self):
        """Adiciona comida à meta do usuário"""
        return GoalController.add_food(get_jwt_identity(), ns.payload)

@ns.route('/diet/remove')
class RemoveDiet(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Deleta comida da meta do usuário')
    @ns.expect(diet_schema)
    @ns.response(200, 'Sucesso', delete_sucess_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def put(self):
        """Deleta comida da meta do usuário"""
        return GoalController.rmv_food(get_jwt_identity(), ns.payload)
