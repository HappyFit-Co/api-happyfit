from flask import request
from flask_restx import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from api.controllers.records import RecordController
from api.schemas.records import (
    ns,
    record_schema,
    workout_schema,
    diet_schema,
    add_diet_schema,
    create_record_schema,
    bad_request_schema,
    unauthorized_schema,
    not_found_schema,
    unprocessable_schema
)

@ns.route('/')
class Record(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Retorna registro do dia.')
    @ns.response(200, 'Sucesso', record_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não Processável', unprocessable_schema)
    def get(self):
        """Lista todo registro do dia"""
        return RecordController.get_daily_record(get_jwt_identity())
    
    @jwt_required()
    @ns.doc(security='jwt', description='Criar registro do dia.')
    @ns.response(201, 'Criado', record_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    @ns.expect(create_record_schema)
    def post(self):
        """Registra as atividade do dia"""
        return RecordController.create_record(get_jwt_identity(), request.json)
    
    @jwt_required()
    @ns.doc(security='jwt', description='Exclui registro do dia.')
    @ns.response(200, 'Sucesso', record_schema)
    @ns.response(400, 'Requisição inválida', bad_request_schema)
    @ns.response(401, 'Não autorizado', unauthorized_schema)
    @ns.response(404, 'Não encontrado', not_found_schema)
    @ns.response(422, 'Entidade não processável', unprocessable_schema)
    def delete(self):
        """Deleta as atividade do dia"""
        return RecordController.delete_record(get_jwt_identity())
    
@ns.route('/water/add/<int:water_volume>')
class RecordAddWater(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Adiciona consumo de água no registro do dia', params={'water_volume': 'Quantidade de água'})
    @ns.expect({'water_volume': int})
    def put(self, water_volume):
        """Adiciona água consumida."""
        return RecordController.add_water_record(get_jwt_identity(), water_volume)
    
@ns.route('/water/remove/<int:water_volume>')
class RecordRemoveWater(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Remove consumo de água no registro do dia', params={'water_volume': 'Quantidade de água'})
    @ns.expect({'water_volume': int})
    def put(self, water_volume):
        """Remove água consumida."""
        return RecordController.remove_water_record(get_jwt_identity(), water_volume)

@ns.route('/workout/add')
class RecordAddWorkout(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Adiciona exercício no registro do dia')
    @ns.expect(workout_schema)
    def put(self):
        """Adiciona exercício no treino do dia."""
        return RecordController.add_workout_record(get_jwt_identity(), request.json)
    
@ns.route('/workout/remove')
class RecordRemoveWorkout(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Remove exercício no registro do dia')
    @ns.expect(workout_schema)
    def put(self):
        """Remove exercício no treino do dia."""
        return RecordController.remove_workout_record(get_jwt_identity(), request.json)
    
@ns.route('/diet/add')
class RecordAddDiet(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Adiciona alimento no registro do dia')
    @ns.expect(add_diet_schema)
    def put(self):
        """Adiciona alimento na dieta do dia."""
        return RecordController.add_diet_record(get_jwt_identity(), request.json)
    
@ns.route('/diet/remove')
class RecordRemoveDiet(Resource):
    @jwt_required()
    @ns.doc(security='jwt', description='Remove alimento no registro do dia')
    @ns.expect(diet_schema)
    def put(self):
        """Remove alimento na dieta do dia."""
        return RecordController.remove_diet_record(get_jwt_identity(), request.json)
