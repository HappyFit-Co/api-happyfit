from bson.objectid import ObjectId

from api.schemas.goals import default_goal
from api.utils.database import mongo


class GoalService:
    # Métodos de CRUD GOAL
    def get_goal(user_id):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            return user["goal"]
        except:
            return {'msg': 'Erro ao obter goal'}, 500

    def edit_goal(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"goal": data}}
            )
            return data
        except:
            return {'msg': 'Erro ao atualizar goal'}, 500

    def delete_goal(user_id):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"goal": {}}}
            )
            return {'msg': 'Meta excluída com sucesso'}, 200
        except:
            return {'msg': 'Erro ao excluir a meta'}, 500


    # Métodos de adicição e remoção
    def add_exercise(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$push": {"goal.workout": data}}
            )
            return {'msg': 'Exercício adicionado com sucesso'}, 200
        except:
            return {'msg': 'Erro ao adicionar exercício'}, 500

    def rmv_exercise(user_id, exercise_id):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$pull": {"goal.workout": {"exercise_id": exercise_id}}}
            )
            return {'msg': 'Exercício removido com sucesso'}, 200
        except:
            return {'msg': 'Erro ao remover exercício'}, 500

    def add_food(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$push": {"goal.diet": data}}
            )
            return {'msg': 'Comida adicionado com sucesso'}, 200
        except:
            return {'msg': 'Erro ao adicionar comida'}, 500
        
    def rmv_food(user_id, food_id):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$pull": {"goal.diet": {"food_id": food_id}}}
            )
            return {'msg': 'Comida removido com sucesso'}, 200
        except:
            return {'msg': 'Erro ao remover comida'}, 500