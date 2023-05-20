from api.services.historics import HistoricService


class HistoricController: 
    def get_historic(user_id):
        return HistoricService.get_historic(user_id)

    def delete_historic(user_id):    
        return HistoricService.clear_historic(user_id)