from flask_restx import Resource
from api.controllers.foodController import FoodController
from api.schemas.foodSchema import ns, food_schema

food_controller = FoodController()

@ns.route('/')
class FoodList(Resource):
    @ns.doc(description='Retorna a lista de dados de alimentos')
    @ns.marshal_list_with(food_schema)
    def get(self):
        """Lista todos os alimentos"""
        return food_controller.get_all_foods()

@ns.route('/id/<string:food_id>')
class FoodById(Resource):
    @ns.doc(description='Retorna dados de um alimento pelo _id', params={'food_id': 'ID do alimento que deseja buscar'})
    @ns.marshal_with(food_schema)
    @ns.expect({'food_id': str})
    def get(self, food_id):
        """Lista alimento pelo _id"""
        return food_controller.get_food_by_id(food_id)

@ns.route('/name/<string:food_name>')
class FoodByName(Resource):
    @ns.doc(description='Retorna dados de alimentos pelo nome', params={'food_name': 'Nome do alimento que deseja buscar'})
    @ns.marshal_with(food_schema)
    @ns.expect({'food_name': str})
    def get(self, food_name):
        """Lista alimentos pelo name"""
        return food_controller.get_food_by_name(food_name)