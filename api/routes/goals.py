from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource

from api.controllers.goals import GoalController
from api.schemas.goals import (diet_parser, diet_schema, goal_schema, ns,
                               workout_parser, workout_schema)


@ns.route('/')
class Goal(Resource):
    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Gerencia a meta do usuário.')
    @ns.response(200, 'Sucesso', [goal_schema])
    def get(self):
        """Retorna a meta do usuário"""
        return GoalController.get_goal(get_jwt_identity())

    @jwt_required()
    @ns.expect(goal_schema)
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Gerencia a meta do usuário.')
    @ns.response(200, 'Sucesso', [goal_schema])
    def post(self):
        """Cria a meta do usuário"""
        return GoalController.post_goal(get_jwt_identity(), request.json)

    @jwt_required()
    @ns.expect(goal_schema)
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Edita a meta do usuário.')
    @ns.response(200, 'Sucesso', [goal_schema])
    def put(self):
        """Edita a meta do usuário"""
        return GoalController.put_goal(get_jwt_identity(), request.json)

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


@ns.route('/workout/remove/<string:exercise_id>')
class RemoveExercise(Resource):
    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Deleta exercício da meta do usuário.')
    def put(self, exercise_id):
        """Deleta exercício da meta do usuário"""
        return GoalController.rmv_exercise(get_jwt_identity(), exercise_id)


@ns.route('/diet/add')
class AddDiet(Resource):
    @jwt_required()
    @ns.expect(diet_schema)
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Adiciona comida à meta do usuário.')
    def put(self):
        """Adiciona comida à meta do usuário"""
        return GoalController.add_food(get_jwt_identity(), diet_parser.parse_args(strict=True))


@ns.route('/diet/remove/<string:food_id>')
class RemoveDiet(Resource):
    @jwt_required()
    @ns.doc(security='jwt', responses={200: 'Sucesso'}, description='Deleta comida da meta do usuário.')
    def put(self, food_id):
        """Deleta comida da meta do usuário"""
        return GoalController.rmv_food(get_jwt_identity(), food_id)
