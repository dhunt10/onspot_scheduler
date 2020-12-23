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

    def get(self):
        args = self.parser.parse_args()
        conn.create_appointment(args.time, args.company, args.date, args.first_name, args.last_name, args.reason, args.phone)
        return "Appointment Created"

api.add_resource(make_appointment, '/make_appointment')

if __name__ == '__main__':
    app.debug = True
    app.run()
