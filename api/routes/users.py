from bson import ObjectId
from flasgger import Swagger, swag_from
from flask import Blueprint, Flask, Response, jsonify, request
from flask_pymongo import PyMongo
from marshmallow import ValidationError

from api.schemas.userSchema import UserSchema

users_bp = Blueprint('users_bp', __name__)

# Rotas e controladores


@users_bp.route('/', methods=['GET'])
def get_users():
    data = []
    return jsonify(data)


@users_bp.route('/<id>', methods=['GET'])
def get_user(id):
    data = id
    return jsonify(data)


@users_bp.route('/', methods=['POST'])
def create_user():

        data = request.get_json()
        user = UserSchema().load(data)
        return jsonify(user)
    