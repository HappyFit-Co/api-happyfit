from flask_jwt_extended import create_access_token, decode_token

from config import Config


def create_token(user_id):
    access_token = create_access_token(identity=str(user_id))
    return access_token

def is_token_valid(token):
    try:
        decoded_token = decode_token(token)    
        return True
    except Exception:
        return False