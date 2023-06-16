from flask_restx import fields
import re
import datetime

from api.schemas.notifications import (
    workout_schema,
    water_schema,
    values_workout_frequency, 
    values_water_frequency)
from api.schemas.users import (
    values_day_of_week,
    values_activity_level
)
from api.services.exercises import ExerciseService
from api.services.foods import FoodService

class InvalidInputException(Exception):
    pass

def validate_data(payload, schema):
    try:
        data = validate_request(payload, schema)
        return data, None
    except InvalidInputException as e:
        return None, str(e)
    
def validate_request(payload, schema):
    validated_data = {}

    for key, field in schema.items():
        if key == 'email':
            if not validate_email(payload.get(key)):
                raise InvalidInputException("Invalid email format")
            validated_data[key] = payload[key]
        elif key in ['date', 'deadline']:
            if not validate_date_format(payload.get(key)):
                raise InvalidInputException("Invalid date format for {}".format(key))
            validated_data[key] = payload[key]
        elif key == 'birthday':
            if not validate_birthday_format(payload.get(key)):
                raise InvalidInputException("Invalid date format for birthday")
            validated_data[key] = payload[key] 
        elif key in ['hour', 'start_hour', 'end_hour']:
            if not validate_hour_format(payload.get(key)):
                raise InvalidInputException("Invalid hour format for {}".format(key))
            validated_data[key] = payload[key]   
            
            # Verificar start_hour < end_hour
            if key == 'start_hour' and 'end_hour' in payload:
                if payload.get(key) >= payload.get('end_hour'):
                    raise InvalidInputException("The start_hour field must be less than end_hour")
        elif key == 'weekday':
            if not validate_day_of_week(payload.get(key)):
                raise InvalidInputException("Invalid weekday")
            validated_data[key] = payload[key]
        elif key == 'activity_level':
            if not validate_activity_level(payload.get(key)):
                raise InvalidInputException("Invalid activity level")
            validated_data[key] = payload[key]
        elif key == 'exercise_id':
            if not validate_exercise_id(payload.get(key)):
                raise InvalidInputException("Invalid exercise id")
            validated_data[key] = payload[key]
        elif key == 'food_id':
            if not validate_food_id(payload.get(key)):
                raise InvalidInputException("Invalid food id")
            validated_data[key] = payload[key]
        else:
            if isinstance(field, fields.Nested):
                if key in payload and isinstance(payload[key], dict):
                    validated_data[key] = validate_request(payload[key], field.model)
            elif isinstance(field, fields.List):
                if key in payload and isinstance(payload[key], list):
                    validated_data[key] = []
                    for item in payload[key]:
                        if isinstance(item, dict):
                            validated_item = validate_request(item, field.container.model)
                            validated_data[key].append(validated_item) 
            else:
                if key in payload:
                    if isinstance(payload[key], (int, float)) and payload[key] < 0:
                        raise InvalidInputException("Invalid negative value for field: {}".format(key))
                    validated_data[key] = payload[key]

                    if key == 'frequency':
                        if all(key in payload for key in workout_schema.keys()):
                            # Pertence à estrutura "workout"
                            if validated_data[key] not in values_workout_frequency:
                                raise InvalidInputException("Invalid frequency for workout")
                        elif all(key in payload for key in water_schema.keys()):
                            # Pertence à estrutura "water"
                            if validated_data[key] not in values_water_frequency:
                                raise InvalidInputException("Invalid frequency for water")
                        else:
                            raise InvalidInputException("Invalid frequency field")

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

def validate_birthday_format(date_string):
    if not validate_date_format(date_string):
        return False
    
    pattern = r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$"
    match = re.match(pattern, date_string)
    year = int(match.group('year'))
    month = int(match.group('month'))
    day = int(match.group('day'))
    
    # Verificação de data de aniversário no futuro
    current_date = datetime.date.today()
    birthday = datetime.date(year, month, day)
    if birthday > current_date:
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
    dias_da_semana = values_day_of_week

    if day.lower() in dias_da_semana:
        return True
    else:
        return False

def validate_activity_level(activity):
    activity_level = values_activity_level

    if activity.lower() in activity_level:
        return True
    else:
        return False
    
def validate_exercise_id(exercise_id):
    exercise, error = ExerciseService.get_exercise_by_id(exercise_id)
    if error:
        return False
    if not exercise:
        return False
    return True
    
def validate_food_id(food_id):
    food, error = FoodService.get_food_by_id(food_id)
    if error:
        return False
    if not food:
        return False
    return True
