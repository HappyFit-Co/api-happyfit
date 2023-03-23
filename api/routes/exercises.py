from bson import ObjectId
from flasgger import Swagger, swag_from
from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo

exercises_bp = Blueprint('exercises_bp', __name__)

# Rotas e controladores

