from flask import request, send_from_directory
from flask_restful import Resource
import os
import sys
sys.path.append(os.path.abspath(os.path.join('../../')))

from models.and_gate import And
from models.or_gate import Or
from models.not_gate import Not 


class Schematic(Resource):
    def post(self):
        os.system("ls")
        os.system("cp -R ../maps/LogiCraft ../maps/LogiCraftCopy")

        req = request.get_json()
        print("yah", req[0]["coordinate"])
        
        for i in range(len(req)):
            for j in range(len(req[i]["inputs"])):
                coord = req[req[i]["inputs"][j]["id"]]["coordinate"]
                req[i]["inputs"][j]["output"] = [coord[0] + 3, coord[1] + 1]
                print("yeet", req[i]["inputs"][j]["output"])

            if req[i]["type"] == "AND":
                gate = And(i, req[i]["inputs"], req[i]["coordinate"]) 

            elif req[i]["type"] == "OR":
                gate = Or(i, req[i]["inputs"], req[i]["coordinate"])

            elif req[i]["type"] == "NOT":
                gate = Not(i, req[i]["inputs"], req[i]["coordinate"])

            else:
                return "bad request", 400
            
            gate.place_redstone() 
            gate.place_gate()

        os.system("cd ../maps/LogiCraftCopy; zip -r ../LogiCraftCopy.zip *")
        os.system("rm -r ../maps/LogiCraftCopy")
        map_file = send_from_directory("../maps/", "LogiCraftCopy.zip", as_attachment=True)
        os.system("rm ../maps/LogiCraftCopy.zip")
        return map_file
