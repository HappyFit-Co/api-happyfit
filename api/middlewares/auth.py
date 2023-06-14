from flask import request, jsonify

from api.security.token import is_token_valid

def middleware(func):
    def wrapper(*args, **kwargs):
        # Verifica se o token de autenticação está presente no header Authorization
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return {'msg': 'Invalid user credentials'}, 401
        
        token = auth_header.split('Bearer ')[1]
        
        # Verifica se o token é válido usando a função is_token_valid
        if not is_token_valid(token):
            return {'msg': 'Invalid user credentials'}, 401
        
        # Chama a função de rota original
        return func(*args, **kwargs)
    
    return wrapper
