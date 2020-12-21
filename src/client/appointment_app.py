from appointment_make import *

from flask import Flask, request, Response
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

conn = appointment_make()

class make_appointment(Resource):
    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('time',
                            type=str,
                            required=True)
        parser.add_argument('company',
                            type=str,
                            required=True)
        parser.add_argument('date',
                            type=str,
                            required=True)
        parser.add_argument('first_name',
                            type=str,
                            required=True)
        parser.add_argument('last_name',
                            type=str,
                            required=True)
        parser.add_argument('reason',
                            type=str,
                            required=True)
        parser.add_argument('phone',
                            type=str,
                            required=True)
        self.parser = parser

api.add_resource(make_appointment, '/add_derma_drive')

if __name__ == '__main__':
    app.debug = True
    app.run()