from datetime import datetime
from bson.objectid import ObjectId

from api.schemas.records import default_record
from api.utils.database import mongo

class RecordService:
    def get_daily_record(user_id):
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            user = mongo.db.users.find_one(
                {"_id": ObjectId(user_id), "historic.date": today},
                {"historic.$": 1}
            )
            return user, None
        except:
            return None, 'Erro interno ao manipular dados no serviço'
    
    def create_record(user_id, record_data):
        try:
            record_id = str(ObjectId())
            today = datetime.now().strftime("%Y-%m-%d")

            record = {
                "_id": record_id,
                "date": today,
                "daily_calories": 0,
                "daily_water": record_data.get("daily_water", 0),
                "daily_macro_nutrient": {
                    "protein": 0,
                    "carbohydrate": 0,
                    "fat": 0
                },
                "workout": [],
                "diet": []
            }

            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

            if user:
                record_list = user.get("historic", [])

                # Procura um registro com a mesma data
                existing_record = next((r for r in record_list if r.get("date") == today), None)

                if existing_record:
                    # Substitui o registro existente com a mesma data
                    existing_record.update(record)
                else:
                    # Adiciona o novo registro à lista
                    record_list.append(record)

                # Atualiza o usuário com o campo historic atualizado
                mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic": record_list}})
            return record_id, None
        except:
            return None, 'Erro interno ao manipular dados no serviço'

    def get_record_by_id(user_id, record_id):
        try:
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            if user and "historic" in user:
                record_list = user["historic"]
                for record in record_list:
                    if record["_id"] == record_id:
                        return record, None
        except:
            return None, 'Erro interno ao manipular dados no serviço'
    
    def delete_record(user_id):
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

            if user and "historic" in user:
                record_list = user["historic"]

                # Encontra o índice do registro com a data de hoje
                index_to_delete = None
                for i, record in enumerate(record_list):
                    if record.get("date") == today:
                        index_to_delete = i
                        break

                if index_to_delete is not None:
                    # Remove o registro da lista
                    del record_list[index_to_delete]

                    # Atualiza o campo historic com a lista atualizada
                    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic": record_list}})
                    
            return None
        except:
            return 'Erro interno ao manipular dados no serviço'

    def add_water_record(user_id, water_volume):
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

            if user and "historic" in user:
                record_list = user["historic"]

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
                    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic": record_list}})
                else:
                    # Cria um novo registro para a data de hoje
                    default_record["daily_water"] = water_volume
                    RecordService.create_record(user_id, default_record)
                    
            return None
        except:
            return 'Erro interno ao manipular dados no serviço'

    def remove_water_record(user_id, water_volume):
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

            if user and "historic" in user:
                record_list = user["historic"]

                # Encontra o índice do registro com a data de hoje
                index_to_update = None
                for i, record in enumerate(record_list):
                    if record.get("date") == today:
                        index_to_update = i
                        break

                if index_to_update is not None:
                    # Remove a quantidade de água do registro
                    record_list[index_to_update]["daily_water"] -= water_volume

                    # Verifica se o valor final de água é negativo e o ajusta para zero
                    if record_list[index_to_update]["daily_water"] < 0:
                        record_list[index_to_update]["daily_water"] = 0

                    # Atualiza o campo historic.record com a lista atualizada
                    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic": record_list}})
                else:
                    # Cria um novo registro para a data de hoje
                    RecordService.create_record(user_id, default_record)

            return None
        except:
            return 'Erro interno ao manipular dados no serviço'
    
    def add_workout_record(user_id, workout):
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

            if user and "historic" in user:
                record_list = user["historic"]

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
                            return None, 'Os dados já existem, evite redundância'

                    # Adiciona o novo exercício à lista de workout do dia de hoje
                    workout_list.append(workout)

                    # Atualiza o campo historic.record com a lista atualizada
                    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic": record_list}})
                else:
                    # Cria um novo registro para a data de hoje
                    default_record["workout"] = [workout]
                    RecordService.create_record(user_id, default_record)
                
            return None, None
        except:
            return 'Erro interno ao manipular dados no serviço', None

    def remove_workout_record(user_id, workout):
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

            if user and "historic" in user:
                record_list = user["historic"]

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
                            mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic": record_list}})

                else:
                    # Cria um novo registro para a data de hoje - sem treino
                    RecordService.create_record(user_id, default_record)

            return None
        except:
            return 'Erro interno ao manipular dados no serviço'
    
    def add_diet_record(user_id, food):
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

            if user and "historic" in user :
                record_list = user["historic"]

                # Encontra o índice do registro com a data de hoje
                index_to_update = None
                for i, record in enumerate(record_list):
                    if record.get("date") == today:
                        index_to_update = i
                        break

                if index_to_update is not None:
                    # Obtém o registro existente
                    existing_record = record_list[index_to_update]

                    # Obtém a lista de diet do registro
                    diet_data = existing_record.get("diet", [])

                    # Adiciona um alimento à lista de diet do registro
                    food_record_id = str(ObjectId())
                    food_record = {
                        "food_record_id": food_record_id,
                        "calories": food.get("calories"),
                        "macro_nutrient": food.get("macro_nutrient"),
                        "hour": food.get("hour")
                    }

                    # Verifica se o alimento já está presente na lista
                    for food_item in diet_data:
                        if food_item.get("calories") == food.get("calories") and \
                        food_item.get("macro_nutrient") == food.get("macro_nutrient") and \
                        food_item.get("hour") == food.get("hour"):
                            return None, 'Os dados já existem, evite redundância'

                    # Adiciona o novo alimento à lista de diet do dia de hoje
                    diet_data.append(food_record)

                    # Calcula o somatório das calorias e macronutrientes da dieta
                    total_calories = sum(item.get("calories", 0) for item in diet_data)
                    total_protein = sum(item.get("macro_nutrient", {}).get("protein", 0) for item in diet_data)
                    total_carbohydrate = sum(item.get("macro_nutrient", {}).get("carbohydrate", 0) for item in diet_data)
                    total_fat = sum(item.get("macro_nutrient", {}).get("fat", 0) for item in diet_data)

                    # Atualiza os valores no registro existente
                    existing_record["daily_calories"] = total_calories
                    existing_record["daily_macro_nutrient"]["protein"] = total_protein
                    existing_record["daily_macro_nutrient"]["carbohydrate"] = total_carbohydrate
                    existing_record["daily_macro_nutrient"]["fat"] = total_fat
                    existing_record["diet"] = diet_data

                    # Atualiza o campo historic.record com o registro atualizado
                    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic": record_list}})
                else:
                    # Cria um novo registro para a data de hoje
                    default_record["diet"] = [food]
                    RecordService.create_record(user_id, default_record)
                
            return None, None
        except:
            return 'Erro interno ao manipular dados no serviço', None
    
    def remove_diet_record(user_id, food):
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

            if user and "historic" in user:
                record_list = user["historic"]

                # Encontra o índice do registro com a data de hoje
                index_to_update = None
                for i, record in enumerate(record_list):
                    if record.get("date") == today:
                        index_to_update = i
                        break

                if index_to_update is not None:
                    # Obtém o registro existente
                    existing_record = record_list[index_to_update]

                    # Obtém a lista de diet do registro
                    diet_data = existing_record.get("diet", [])

                    # Procura o alimento na lista de diet do registro
                    for food_item in diet_data:
                        if food_item == food:
                            diet_data.remove(food_item)

                            # Subtrai as calorias e macronutrientes do alimento removido
                            existing_record["daily_calories"] -= food_item.get("calories", 0)
                            existing_record["daily_macro_nutrient"]["protein"] -= food_item.get("macro_nutrient", {}).get("protein", 0)
                            existing_record["daily_macro_nutrient"]["carbohydrate"] -= food_item.get("macro_nutrient", {}).get("carbohydrate", 0)
                            existing_record["daily_macro_nutrient"]["fat"] -= food_item.get("macro_nutrient", {}).get("fat", 0)

                            existing_record["diet"] = diet_data

                            # Atualiza o campo historic.record com o registro atualizado
                            mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"historic": record_list}})
                else:
                    # Cria um novo registro para a data de hoje - sem treino
                    RecordService.create_record(user_id, default_record)

            return None
        except:
            return 'Erro interno ao manipular dados no serviço'
