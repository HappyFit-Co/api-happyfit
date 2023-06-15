from api.services.historics import HistoricService

class HistoricController: 
    def get_historic(user_id):
        historic, error = HistoricService.get_historic(user_id)
        if error:
            return {'msg': error}, 500
        return historic, 200

    def delete_historic(user_id):    
        error = HistoricService.clear_historic(user_id)
        if error:
            return {'msg': error}, 500
        return {'msg': 'Excluído com sucesso'}, 200