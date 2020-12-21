from query import admin_connection
from flask import Flask, request, Response
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

conn = admin_connection()

class HealthCheck(Resource):

    def get(self):
        return {'status':'alive'}, 200

class post_company(Resource):
    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name',
                            type=str,
                            required=True)
        parser.add_argument('address',
                            type=str,
                            required=True)
        self.parser = parser

    def get(self):
        args = self.parser.parse_args()
        conn.create_company(args.name, args.address)
        return "Posted"

class add_provider(Resource):
    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name',
                            type=str,
                            required=True)
        self.parser = parser

    def get(self):
        args = self.parser.parse_args()
        conn.add_provider(args.name)
        return "Posted"

class add_patient(Resource):
    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('company_name',
                            type=str,
                            required=True)
        parser.add_argument('first_name',
                            type=str,
                            required=True)
        parser.add_argument('last_name',
                            type=str,
                            required=True)
        parser.add_argument('email',
                            type=str,
                            required=True)
        parser.add_argument('dob',
                            type=str,
                            required=True)
        parser.add_argument('member_id',
                            type=str,
                            required=True)
        parser.add_argument('group_id',
                            type=str,
                            required=True)
        parser.add_argument('provider_name',
                            type=str,
                            required=True)
        parser.add_argument('phone',
                            type=str,
                            required=True)
        parser.add_argument('note',
                            type=str,
                            required=False)
        self.parser = parser

    def get(self):
        args = self.parser.parse_args()
        conn.create_patient(args.company_name,
                            args.first_name,
                            args.last_name,
                            args.email,
                            args.dob,
                            args.member_id,
                            args.group_id,
                            args.provider_name,
                            args.phone,
                            args.note)
        return "Posted"

class add_doctor(Resource):
    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('doctor_name',
                            type=str,
                            required=True)
        self.parser = parser

    def get(self):
        args = self.parser.parse_args()
        conn.create_doctor(args.doctor_name)

class add_head_contact(Resource):
    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('contact_name',
                            type=str,
                            required=True)
        parser.add_argument('company_name',
                            type=str,
                            required=True)
        parser.add_argument('email',
                            type=str,
                            required=True)
        parser.add_argument('note',
                            type=str,
                            required=False)
        parser.add_argument('phone',
                            type=str,
                            required=False)
        self.parser = parser

    def get(self):
        args = self.parser.parse_args()
        conn.add_head_contact(args.contact_name,
                              args.company_name,
                              args.email,
                              args.note,
                              args.phone)

class add_derma_drive(Resource):
    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('company_name',
                            type=str,
                            required=True)
        parser.add_argument('year',
                            type=str,
                            required=True)
        parser.add_argument('month',
                            type=str,
                            required=True)
        parser.add_argument('day',
                            type=str,
                            required=True)
        parser.add_argument('start_time',
                            type=str,
                            required=True)
        parser.add_argument('end_time',
                            type=str,
                            required=True)
        self.parser = parser

    def get(self):
        args = self.parser.parse_args()
        date = args.year + '-' + args.month + '-' + args.day
        conn.add_derma_drive(args.company_name, date, args.start_time, args.end_time)

api.add_resource(HealthCheck, '/')
api.add_resource(post_company, '/add_company')
api.add_resource(add_provider, '/add_provider')
api.add_resource(add_patient, '/add_patient')
api.add_resource(add_doctor, '/add_doctor')
api.add_resource(add_head_contact, '/add_head_contact')
api.add_resource(add_derma_drive, '/add_derma_drive')

if __name__ == '__main__':
    app.debug = True
    app.run()
