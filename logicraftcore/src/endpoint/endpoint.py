from flask import request, send_from_directory
from flask_restful import Resource
import os

class Schematic(Resource):
    def post(self):
        req = request.get_json()

        os.system("ls")
        os.system("cp -Ri ../maps/LogiCraft ../maps/LogiCraftCopy")
        os.system("cd ../maps/LogiCraftCopy; zip -r ../LogiCraftCopy.zip *")
        os.system("rm -r ../maps/LogiCraftCopy")
        map_file = send_from_directory("../maps/", "LogiCraftCopy.zip", as_attachment=True)
        os.system("rm ../maps/LogiCraftCopy.zip")
        return map_file

    def get(self):
        return send_from_directory("../maps/", "LogiCraftCopy.zip", as_attachment=True) 