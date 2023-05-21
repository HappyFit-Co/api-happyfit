from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource

from api.controllers.goals import GoalController
from api.schemas.goals import (
    ns,
    goal_schema,
    workout_schema,
    diet_schema,
    goal_parser,
    workout_parser,
    diet_parser
    )
from api.schemas.response import (
    unauthorized_schema,
    empty_list_schema,
    not_found_schema,
    unprocessable_schema,
    internal_server_schema
)

@ns.route('/')
class Goal(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna a meta do usuário')
    @ns.response(200, 'Sucesso', [goal_schema])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', empty_list_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def get(self):
        """Vizualiza a meta do usuário"""
        return GoalController.get_goal(get_jwt_identity())

    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Gerencia a meta do usuário.')
    @ns.expect(goal_schema)
    @ns.response(200, 'Sucesso', [goal_schema])
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', empty_list_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.response(500, 'Erro interno do servidor', internal_server_schema)
    def post(self):
        """Cria a meta do usuário"""
        return GoalController.post_goal(get_jwt_identity(), goal_parser.parse_args(request, strict=True))

    @jwt_required()
    @ns.expect(goal_schema)
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Edita a meta do usuário.')
    @ns.response(200, 'Sucesso', [goal_schema])
    def put(self):
        """Edita a meta do usuário"""
        return GoalController.put_goal(get_jwt_identity(), goal_parser.parse_args(request, strict=True))

    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Deleta a meta do usuário.')
    @ns.response(200, 'Sucesso', [goal_schema])
    def delete(self):
        """Deleta a meta do usuário"""
        return GoalController.delete_goal(get_jwt_identity())


@ns.route('/workout/add')
class AddExercise(Resource):
    @jwt_required()
    @ns.expect(workout_schema)
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Adiciona exercício à meta do usuário.')
    def put(self):
        """Adiciona exercício à meta do usuário"""
        return GoalController.add_exercise(get_jwt_identity(), workout_parser.parse_args(strict=True))


@ns.route('/workout/remove')
class RemoveExercise(Resource):
    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Deleta exercício da meta do usuário.')
    def put(self):
        """Deleta exercício da meta do usuário"""
        return GoalController.rmv_exercise(get_jwt_identity(), workout_parser.parse_args(strict=True))


@ns.route('/diet/add')
class AddDiet(Resource):
    @jwt_required()
    @ns.expect(diet_schema)
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Adiciona comida à meta do usuário.')
    def put(self):
        """Adiciona comida à meta do usuário"""
        return GoalController.add_food(get_jwt_identity(), diet_parser.parse_args(strict=True))


@ns.route('/diet/remove')
class RemoveDiet(Resource):
    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Deleta comida da meta do usuário.')
    def put(self):
        """Deleta comida da meta do usuário"""
        return GoalController.rmv_food(get_jwt_identity(), diet_parser.parse_args(strict=True))
