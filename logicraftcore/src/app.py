from flask import Flask
from flask_restful import Resource, Api
from endpoint.endpoint import Schematic

app = Flask(__name__)
api = Api(app)

api.add_resource(Schematic, '/api/schematic')

if __name__ == '__main__': 
    app.run(debug=True)