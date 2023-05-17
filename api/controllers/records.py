from api.services.records import RecordService
       
class RecordController:
    def get_daily_record(user_id):
        user = RecordService.get_daily_record(user_id)
        if user and "historic" in user and "record" in user["historic"] and len(user["historic"]["record"]) > 0:
            return user["historic"]["record"][0], 200
        else:
            return {'msg': 'Requested resource not found'}, 404
        
    def create_record(user_id, record_data):
        record_id = RecordService.create_record(user_id, record_data)
        if not record_id:
            return {'msg': 'Invalid request due to errors or inappropriate customer data'}, 400
        record = RecordService.get_record_by_id(user_id, record_id)
        if not record:
            return {'msg': 'Requested resource not found'}, 404
        return record, 201

        
