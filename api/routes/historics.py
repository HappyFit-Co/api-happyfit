from bson import ObjectId
from flasgger import Swagger, swag_from
from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo

historics_bp = Blueprint('historics_bp', __name__)

# Rotas e controladores

