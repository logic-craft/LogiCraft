from flask import request
from flask_restful import Resource

class Schematic(Resource):
    def post(self):
        req = request.get_json()
        for key, value in req.items():
            print(key)
        return req