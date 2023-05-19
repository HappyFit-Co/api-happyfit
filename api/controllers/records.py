from api.services.records import RecordService
from api.utils.validate import validate_create_record_schema
from api.schemas.records import create_record_schema
       
class RecordController:
    def get_daily_record(user_id):
        user = RecordService.get_daily_record(user_id)
        if user and "historic" in user and "record" in user["historic"] and len(user["historic"]["record"]) > 0:
            return user["historic"]["record"][0], 200
        else:
            return {'msg': 'Requested resource not found'}, 404
        
    def create_record(user_id, record_data):
        # Realizar a validação completa dos dados recebidos
        error = validate_create_record_schema(record_data)
        if error:
            return {'msg': error}, 400
        
        record_id = RecordService.create_record(user_id, record_data)
        if not record_id:
            return {'msg': 'Invalid request due to errors or inappropriate customer data'}, 500
        
        record = RecordService.get_record_by_id(user_id, record_id)
        if not record:
            return {'msg': 'Requested resource not found'}, 404
        return record, 201

    def delete_record(user_id):
        status = RecordService.delete_record(user_id)
        if status == 400:
            return {'msg': 'Invalid request due to errors or inappropriate customer data'}, 400
        elif status == 404:
            return {'msg': 'Requested resource not found'}, 404
        else:
            return {'msg': 'Record of the day deleted successfully'}, 200
        
    def add_water_record(user_id, water_volume):
        if water_volume < 0:
            water_volume = 0
        
        error = RecordService.add_water_record(user_id, water_volume)
        if error:
            return {'msg': error}, 404
        return {'msg': 'Success in adding water'}, 200
    
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

        
