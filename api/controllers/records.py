from flask_restx import marshal

from api.schemas.records import (
    record_schema, 
    create_record_schema, 
    workout_schema,
    diet_schema,
    add_diet_schema,
    default_record
)
from api.services.records import RecordService
from api.utils.validate import validate_data

class RecordController:
    def get_daily_record(user_id):
        user, error = RecordService.get_daily_record(user_id)
        if error:
            return {'msg': error}, 500
        if not (user and "historic" in user and len(user["historic"]) > 0):
            return RecordController().create_record(user_id, default_record)
        return marshal(user["historic"][0], record_schema), 200
      
    @staticmethod
    def create_record(user_id, data):
        record_data, error = validate_data(data, create_record_schema)
        if error:
            return {'msg': error}, 400
        
        record_id, error = RecordService.create_record(user_id, record_data)
        if error:
            return {'msg': error}, 500
        if not record_id:
            return {'msg': 'Dados de entrada inválidos ou incompletos'}, 400
        
        for workout_data in record_data.get('workout', []):
            response, _ = RecordController().add_workout_record(user_id, workout_data)
            if response.get('msg') != 'Adicionado com sucesso':
                return response, 400
        
        for diet_data in record_data.get('diet', []):
            response, _ = RecordController().add_diet_record(user_id, diet_data)
            if response.get('msg') != 'Adicionado com sucesso':
                return response, 400
        
        record, error = RecordService.get_record_by_id(user_id, record_id)
        if error:
            return {'msg': error}, 500
        if not record:
            return {'msg': 'Nenhum dado encontrado'}, 404
        return marshal(record, record_schema), 201
    
    def delete_record(user_id):
        error = RecordService.delete_record(user_id)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Excluído com sucesso'}, 200
        
    def add_water_record(user_id, water_volume):
        if water_volume < 0:
            water_volume = 0
        
        error = RecordService.add_water_record(user_id, water_volume)
        if error:
            return {'msg': error}, 404
        return {'msg': 'Adicionado com sucesso'}, 200
    
    def remove_water_record(user_id, water_volume):
        if water_volume < 0:
            water_volume = 0
            
        error = RecordService.remove_water_record(user_id, water_volume)
        if error:
            return {'msg': error}, 404
        return {'msg': 'Excluído com sucesso'}, 200
    
    @staticmethod
    def add_workout_record(user_id, data):
        exercise, error = validate_data(data, workout_schema)
        if error:
            return {'msg': error}, 400
        
        error, redundancy = RecordService.add_workout_record(user_id, exercise)
        if error:
            return {'msg': error}, 500
        if redundancy:
            return {'msg': redundancy}, 400
        return {'msg': 'Adicionado com sucesso'}, 200
    
    def remove_workout_record(user_id, data):
        exercise, error = validate_data(data, workout_schema)
        if error:
            return {'msg': error}, 400
        
        error = RecordService.remove_workout_record(user_id, exercise)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Excluído com sucesso'}, 200
    
    @staticmethod
    def add_diet_record(user_id, data):
        food, error = validate_data(data, add_diet_schema)
        if error:
            return {'msg': error}, 400
        
        error, redundancy = RecordService.add_diet_record(user_id, food)
        if error:
            return {'msg': error}, 500
        if redundancy:
            return {'msg': redundancy}, 400
        return {'msg': 'Adicionado com sucesso'}, 200
    
    def remove_diet_record(user_id, data):
        food, error = validate_data(data, diet_schema)
        if error:
            return {'msg': error}, 400
        
        error = RecordService.remove_diet_record(user_id, food)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Excluído com sucesso'}, 200
