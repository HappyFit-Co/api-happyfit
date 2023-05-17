from bson.objectid import ObjectId

from api.utils.database import mongo


class GoalService:
    def get_goal(user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return user["goal"]


    def edit_goal(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"goal": data}}
            )
            return data, 200
        except:
            return {'message': 'Erro ao atualizar configuração'}, 400

    def delete_goal(user_id):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$unset": {"goal": ""}}
            )
            return {'message': 'Meta excluída com sucesso'}, 200
        except:
            return {'message': 'Erro ao excluir a meta'}, 400

    def add_exercise(user_id, data):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$push": {"goal.workout": data}}
            )
            return {'message': 'Exercício adicionado com sucesso'}, 200
        except:
            return {'message': 'Erro ao adicionar exercício'}, 400

    def rmv_exercise(user_id, exercise_id):
        try:
            mongo.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$pull": {"goal.workout": {"exercise_id": exercise_id}}}
            )
            return {'message': 'Exercício removido com sucesso'}, 200
        except:
            return {'message': 'Erro ao remover exercício'}, 400
