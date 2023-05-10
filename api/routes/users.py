from flask import request
from flask_apispec import marshal_with
from flask_apispec.views import MethodResource
from flask_restful import Resource
from marshmallow import Schema, fields


class AwesomeResponseSchema(Schema):
    message = fields.Str(default='Success')

class Users(MethodResource, Resource):
    @marshal_with(AwesomeResponseSchema)
    def get(self):
        return {'Response':"GET"}
    def post(self):
        return {'Response':"POST"}, 201

    def put(self, user_id):
        return {"ID":user_id}, 200

    def delete(self, user_id):
        return {"ID":user_id}, 200