from api.services.records import RecordService

class RecordController: 
    def __init__(self):
        self.record_service = RecordService()