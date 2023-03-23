from bson import ObjectId
from flasgger import Swagger, swag_from
from flask import Blueprint, Flask, Response, jsonify, request
from flask_pymongo import PyMongo

from api.schemas.userSchema import UserSchema

users_bp = Blueprint('users_bp', __name__)

# Rotas e controladores

@users_bp.route('/', methods=['GET'])
def get_users():
    """
    Endpoint para listar todos os usuários
    ---
    responses:
      200:
        description: Lista de todos os usuários
        schema:
          type: array
          items:
            $ref: '#/definitions/User'
    """
    try:
        pass
    except Exception:
        return Response('Error Message', 400)
    
    return jsonify({"Message":"Teste"})
