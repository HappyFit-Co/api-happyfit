from flask_restx import inputs

from api.schemas.foods import macro_schema
from api.schemas.records import (
    create_record_schema,
    workout_schema,
    diet_schema
)

def validate_email(email):
    if not inputs.regex(r'^[\w\.-]+@[\w\.-]+\.\w+$', error='Invalid email format').__call__(email):
        raise ValueError('Invalid email format')
    
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
    
def validate_create_record_schema(data):
    try:
        # Verificar se todos os campos estão presentes
        record_fields = set(create_record_schema.__schema__['properties'].keys())
        if record_fields != set(data.keys()):
            missing_fields = record_fields - set(data.keys())
            if missing_fields:
                return f"Missing fields: {missing_fields}"
            else:
                extra_fields = set(data.keys()) - record_fields
                return f"There are extra attributes beyond the specified fields: {extra_fields}"

        # Verificar a estrutura dos dados em workout
        for i, workout in enumerate(data['workout'], start=1):
            workout_fields = set(workout_schema.__schema__['properties'].keys())
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
                missing_fields = macro_fields - set(diet['macro_nutrient'].keys())
                if missing_fields:
                    return f"Missing fields in macro_nutrient of diet {i}: {missing_fields}"
                else:
                    extra_fields = set(diet['macro_nutrient'].keys()) - macro_fields
                    return f"There are extra attributes in macro_nutrient of diet {i} beyond the specified fields: {extra_fields}"

            if not validate_hour_format(diet['hour']):
                return f"Invalid hour format in diet {i}"

        return None
    except Exception as e:
        return str(e)










        
        