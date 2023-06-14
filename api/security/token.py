from flask_jwt_extended import create_access_token, decode_token

def create_token(user_id):
    access_token = create_access_token(identity=str(user_id))
    return access_token

def is_token_valid(token):
    try:
        decoded_token = decode_token(token)    
        return True
    except Exception:
        return False
    
def get_claims(request):
    token = request.headers.get('Authorization')
    if not token or not token.startswith('Bearer '):
        return None
    
    token = token.split('Bearer ')[1]
    
    try:
        decoded_token = decode_token(token)
        user_id = decoded_token['sub']
        return user_id

    except Exception:
        return None
    