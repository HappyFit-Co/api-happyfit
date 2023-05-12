from flask import request
from flask_restx import Resource, Namespace, fields


api = Namespace('users', description='User operations')

class AwesomeResponseSchema(fields.Raw):
    def format(self, value):
        return {'message': value or 'Success'}

class Users(Resource):
    @api.marshal_with(AwesomeResponseSchema())
    def get(self):
        return {'Response': "GET"}

    @api.doc(responses={201: 'Created'})
    @api.marshal_with(AwesomeResponseSchema())
    def post(self):
        return {'Response': "POST"}, 201

    @api.doc(params={'user_id': 'User ID'})
    def put(self, user_id):
        return {"ID": user_id}, 200

    @api.doc(params={'user_id': 'User ID'})
    def delete(self, user_id):
        return {"ID": user_id}, 200

api.add_resource(Users, '/')
