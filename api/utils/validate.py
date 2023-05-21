from flask_restx import fields
import re, json

from api.schemas.foods import macro_schema
from api.schemas.records import (create_record_schema, diet_schema,
                                 workout_schema)

def validate_request(payload, schema):
    validated_data = {}

    for key, field in schema.items():
        if isinstance(field, fields.Nested):
            if key in payload and isinstance(payload[key], dict):
                validated_data[key] = validate_request(payload[key], field.model)
        elif isinstance(field, fields.List):
            if key in payload and isinstance(payload[key], list):
                validated_data[key] = []
                for item in payload[key]:
                    if isinstance(item, dict):
                        validated_item = validate_request(item, field.container)
                        validated_data[key].append(validated_item)
        else:
            if key in payload:
                validated_data[key] = payload[key]
    return validated_data

def validate_email(email):
    # Expressão regular para validar o formato de um email
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Verifica se o email corresponde ao padrão da expressão regular
    if re.match(email_pattern, email):
        return True
    else:
        return False

def validate_date_format(date_string):
    pattern = r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$"
    match = re.match(pattern, date_string)
    if not match:
        return False

    year = int(match.group('year'))
    month = int(match.group('month'))
    day = int(match.group('day'))

    # Restrições de valores
    if year <= 0 or month <= 0 or month > 12 or day <= 0 or day > 31:
        return False

    # Restrições adicionais
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        elif day > 28:
            return False

    return True

def validate_hour_format(hour):
    try:
        if len(hour) != 5:
            return False

        hour_parts = hour.split(':')
        if len(hour_parts) != 2:
            return False

        hour_value = int(hour_parts[0])
        minute_value = int(hour_parts[1])

        if hour_value < 0 or hour_value > 23:
            return False

        if minute_value < 0 or minute_value > 59:
            return False

        return True
    except ValueError:
        return False

def validate_day_of_week(day):
    dias_da_semana = ['segunda-feira', 'terça-feira', 'quarta-feira',
                      'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

    if day.lower() in dias_da_semana:
        return True
    else:
        return False

def validate_create_record_schema(data):
    try:
        # Verificar se todos os campos estão presentes
        record_fields = set(create_record_schema.__schema__[
                            'properties'].keys())
        if record_fields != set(data.keys()):
            missing_fields = record_fields - set(data.keys())
            if missing_fields:
                return f"Missing fields: {missing_fields}"
            else:
                extra_fields = set(data.keys()) - record_fields
                return f"There are extra attributes beyond the specified fields: {extra_fields}"

        # Verificar a estrutura dos dados em workout
        for i, workout in enumerate(data['workout'], start=1):
            workout_fields = set(workout_schema.__schema__[
                                 'properties'].keys())
            if workout_fields != set(workout.keys()):
                missing_fields = workout_fields - set(workout.keys())
                if missing_fields:
                    return f"Missing fields in workout {i}: {missing_fields}"
                else:
                    extra_fields = set(workout.keys()) - workout_fields
                    return f"There are extra attributes in workout {i} beyond the specified fields: {extra_fields}"

            if not validate_hour_format(workout['hour']):
                return f"Invalid hour format in workout {i}"

        # Verificar a estrutura dos dados em diet
        for i, diet in enumerate(data['diet'], start=1):
            diet_fields = set(diet_schema.__schema__['properties'].keys())
            macro_fields = set(macro_schema.__schema__['properties'].keys())
            if diet_fields != set(diet.keys()):
                missing_fields = diet_fields - set(diet.keys())
                if missing_fields:
                    return f"Missing fields in diet {i}: {missing_fields}"
                else:
                    extra_fields = set(diet.keys()) - diet_fields
                    return f"There are extra attributes in diet {i} beyond the specified fields: {extra_fields}"

            if not isinstance(diet['macro_nutrient'], dict):
                return f"macro_nutrient in diet {i} is not a dictionary"

            if macro_fields != set(diet['macro_nutrient'].keys()):
                missing_fields = macro_fields - \
                    set(diet['macro_nutrient'].keys())
                if missing_fields:
                    return f"Missing fields in macro_nutrient of diet {i}: {missing_fields}"
                else:
                    extra_fields = set(
                        diet['macro_nutrient'].keys()) - macro_fields
                    return f"There are extra attributes in macro_nutrient of diet {i} beyond the specified fields: {extra_fields}"

            if not validate_hour_format(diet['hour']):
                return f"Invalid hour format in diet {i}"

        return None
    except Exception as e:
        return str(e)

def validate_model_data(model, data, model_name):
    try:
        # Verificar se todos os campos estão presentes
        model_fields = set(model.__schema__['properties'].keys())
        
        if model_fields != set(data.keys()):
            missing_fields = model_fields - set(data.keys())
            if missing_fields:
                return f"Missing fields in {model_name}: {missing_fields}"
            else:
                extra_fields = set(data.keys()) - model_fields
                return f"There are extra attributes in {model_name} beyond the specified fields: {extra_fields}"

        # Verificar a estrutura dos dados
        for i, item in enumerate(data, start=1):
            # Verificar campos aninhados recursivamente
            for nested_model_name, nested_model in model.__schema__['properties'].items():
                if nested_model_name in item and isinstance(nested_model, dict):
                    error = validate_model_data(nested_model, item[nested_model_name], nested_model_name)
                    if error:
                        return error

            # Verificar campo de data (AAAA-MM-DD)
            if 'date' in item:
                if not validate_date_format(item['date']):
                    return f"Invalid date format in {model_name} {i}"

            # Verificar campo de hora (HH:MM)
            if 'hour' in item:
                if not validate_hour_format(item['hour']):
                    return f"Invalid hour format in {model_name} {i}"

        return None
    except Exception as e:
        return str(e)

def validate_macro_schema(macro_nutrients_data):
    macro_fields = set(macro_schema.__schema__['properties'].keys())
    if macro_fields != set(macro_nutrients_data.keys()):
        missing_fields = macro_fields - set(macro_nutrients_data.keys())
        if missing_fields:
            return f"Missing fields in macro_nutrient of diet: {missing_fields}"
        else:
            extra_fields = set(macro_nutrients_data.keys()) - macro_fields
            return f"There are extra attributes in macro_nutrient beyond the specified fields: {extra_fields}"
    return None

def validate_exercise_goal(exercise_data):
    error = None if validate_hour_format(
        exercise_data["hour"]) else "Error validating the hour format. Correct format (HH:MM)."
    error = None if validate_day_of_week(
        exercise_data["weekday"]) else "Error validating the day of the week."
    return error

def validate_food_goal(exercise_data):
    error = None if validate_day_of_week(
        exercise_data["weekday"]) else "Error validating the day of the week."
    return error
