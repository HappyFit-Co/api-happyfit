from api.utils.database import mongo
from bson.objectid import ObjectId
from datetime import datetime

class RecordService:
    def get_daily_record(user_id):
        today = datetime.now().strftime("%Y-%m-%d")
        user = mongo.db.users.find_one(
            {"_id": ObjectId(user_id), "historic.record.date": today},
            {"historic.record.$": 1}
        )
        return user
    
    def create_record(user_id, record_data):
        record_id = str(ObjectId())
        today = datetime.now().strftime("%Y-%m-%d")
        diet_data = record_data.get("diet", [])

        # Calcula o somatório das calorias e macronutrientes da dieta
        total_calories = sum(item.get("calories", 0) for item in diet_data)
        total_protein = sum(item.get("macro_nutrient", {}).get("protein", 0) for item in diet_data)
        total_carbohydrate = sum(item.get("macro_nutrient", {}).get("carbohydrate", 0) for item in diet_data)
        total_fat = sum(item.get("macro_nutrient", {}).get("fat", 0) for item in diet_data)

        record = {
            "_id": record_id,
            "date": today,
            "daily_calories": total_calories,
            "daily_water": record_data.get("daily_water", 0),
            "daily_macro_nutrient": {
                "protein": total_protein,
                "carbohydrate": total_carbohydrate,
                "fat": total_fat
            },
            "workout": record_data.get("workout", []),
            "diet": diet_data
        }

        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

        if user:
            historic = user.get("historic", {})
            record_list = historic.get("record", [])

            # Procura um registro com a mesma data
            existing_record = next((r for r in record_list if r.get("date") == today), None)

            if existing_record:
                # Substitui o registro existente com a mesma data
                existing_record.update(record)
            else:
                # Adiciona o novo registro à lista
                record_list.append(record)

            # Atualiza o campo historic.record com a lista atualizada
            historic["record"] = record_list

            # Atualiza o usuário com o campo historic atualizado
            mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic": historic}})
        return record_id

    def get_record_by_id(user_id, record_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if user and "historic" in user and "record" in user["historic"]:
            record_list = user["historic"]["record"]
            for record in record_list:
                if record["_id"] == record_id:
                    return record
        return None
    
    def delete_record(user_id):
        today = datetime.now().strftime("%Y-%m-%d")

        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

        if user and "historic" in user and "record" in user["historic"]:
            record_list = user["historic"]["record"]

            # Encontra o índice do registro com a data de hoje
            index_to_delete = None
            for i, record in enumerate(record_list):
                if record.get("date") == today:
                    index_to_delete = i
                    break

            if index_to_delete is not None:
                # Remove o registro da lista
                del record_list[index_to_delete]

                # Atualiza o campo historic.record com a lista atualizada
                mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic.record": record_list}})
                return 200
            else:
                return 404

        return 404
    
    from datetime import datetime

    def add_water_record(user_id, water_volume):
        today = datetime.now().strftime("%Y-%m-%d")

        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

        if user and "historic" in user and "record" in user["historic"]:
            record_list = user["historic"]["record"]

            # Encontra o índice do registro com a data de hoje
            index_to_update = None
            for i, record in enumerate(record_list):
                if record.get("date") == today:
                    index_to_update = i
                    break

            if index_to_update is not None:
                # Atualiza a quantidade de água do registro
                record_list[index_to_update]["daily_water"] += water_volume

                # Atualiza o campo historic.record com a lista atualizada
                mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic.record": record_list}})
                return None
            else:
                return f"No record of the day found"

        return f"No record history found"
    
    def add_workout_record(user_id, workout):
        today = datetime.now().strftime("%Y-%m-%d")

        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

        if user and "historic" in user and "record" in user["historic"]:
            record_list = user["historic"]["record"]

            # Encontra o índice do registro com a data de hoje
            index_to_update = None
            for i, record in enumerate(record_list):
                if record.get("date") == today:
                    index_to_update = i
                    break

            if index_to_update is not None:
                # Obtém a lista de workout do registro
                workout_list = record_list[index_to_update].get("workout", [])

                # Verifica se o exercício já está presente na lista
                for workout_item in workout_list:
                    if workout_item == workout:
                        return "Exercise already exists in today's workout"

                # Adiciona o novo exercício à lista de workout do dia de hoje
                workout_list.append(workout)

                # Atualiza o campo historic.record com a lista atualizada
                mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic.record": record_list}})
                return None
            else:
                return "No record of the day found"

        return "No record history found"

    def remove_workout_record(user_id, workout):
        today = datetime.now().strftime("%Y-%m-%d")

        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

        if user and "historic" in user and "record" in user["historic"]:
            record_list = user["historic"]["record"]

            # Encontra o índice do registro com a data de hoje
            index_to_update = None
            for i, record in enumerate(record_list):
                if record.get("date") == today:
                    index_to_update = i
                    break

            if index_to_update is not None:
                # Obtém a lista de workout do registro
                workout_list = record_list[index_to_update].get("workout", [])

                # Verifica se o exercício está presente na lista
                for workout_item in workout_list:
                    if workout_item == workout:
                        workout_list.remove(workout_item)

                        # Atualiza o campo historic.record com a lista atualizada
                        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic.record": record_list}})
                        return None

                return "Exercise not found in today's workout"

            else:
                return "No record of the day found"

        return "No record history found"



