from flask_restx import marshal

from api.schemas.records import create_record_schema, record_schema
from api.services.records import RecordService
from api.utils.validate import validate_create_record_schema


class RecordController:
    def get_daily_record(user_id):
        user, error = RecordService.get_daily_record(user_id)
        if error:
            return {'msg': error}, 500
        if not (user and "historic" in user and len(user["historic"]) > 0):
            return {'msg': "No data was found"}, 404
        return marshal(user["historic"][0], record_schema), 200
      
    def create_record(user_id, record_data):
        record_id, error = RecordService.create_record(user_id, record_data)
        if error:
            return {'msg': error}, 500
        if not record_id:
            return {'msg': 'Invalid or incomplete input data'}, 400
        
        record, error = RecordService.get_record_by_id(user_id, record_id)
        if error:
            return {'msg': error}, 500
        if not record:
            return {'msg': 'No data was found'}, 404
        return marshal(record, record_schema), 201
    
    def delete_record(user_id):
        error = RecordService.delete_record(user_id)
        if error:
            return {'msg': error}, 500
        return {'msg': "Successfully deleted"}, 200
        
    def add_water_record(user_id, water_volume):
        if water_volume < 0:
            water_volume = 0
        
        error = RecordService.add_water_record(user_id, water_volume)
        if error:
            return {'msg': error}, 404
        return {'msg': 'Successfully updated'}, 200
    
    def remove_water_record(user_id, water_volume):
        if water_volume < 0:
            water_volume = 0
            
        error = RecordService.remove_water_record(user_id, water_volume)
        if error:
            return {'msg': error}, 404
        return {'msg': 'Successfully updated'}, 200
    
    def add_workout_record(user_id, exercise):
        error = RecordService.add_workout_record(user_id, exercise)
        if error:
            return {'msg': error}, 404
        return {'msg': 'Success in adding exercise'}, 200
    
    def remove_workout_record(user_id, exercise):
        error = RecordService.remove_workout_record(user_id, exercise)
        if error:
            return {'msg': error}, 404
        return {'msg': 'Success in removing exercise'}, 200
    
    def add_diet_record(user_id, food):
        error = RecordService.add_diet_record(user_id, food)
        if error:
            return {'msg': error}, 404
        return {'msg': 'Success in adding food'}, 200
    
    def remove_diet_record(user_id, food):
        error = RecordService.remove_diet_record(user_id, food)
        if error:
            return {'msg': error}, 404
        return {'msg': 'Success in removing food'}, 200

        
