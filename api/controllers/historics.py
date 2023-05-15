from api.services.historics import HistoricService

class HistoricController: 
    def __init__(self):
        self.historic_service = HistoricService()