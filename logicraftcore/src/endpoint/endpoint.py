from flask import request, send_from_directory
from flask_restful import Resource
import os
import sys
sys.path.append(os.path.abspath(os.path.join('../../')))

from models.gate import Gate



class Schematic(Resource):
    def post(self):
        req = request.get_json()

        os.system("ls")
        os.system("cp -R ../maps/LogiCraft ../maps/LogiCraftCopy")


        gate = Gate(1, {
            "points": [[4, 3], [0, 3]],
            "output": [4, 5]
        }, [1, 0])

        gate.place_redstone()
        os.system("cd ../maps/LogiCraftCopy; zip -r ../LogiCraftCopy.zip *")
        # os.system("rm -r ../maps/LogiCraftCopy")
        # map_file = send_from_directory("../maps/", "LogiCraftCopy.zip", as_attachment=True)
        # os.system("rm ../maps/LogiCraftCopy.zip")
        # return map_file

    def get(self):
        return send_from_directory("../maps/", "LogiCraftCopy.zip", as_attachment=True) 