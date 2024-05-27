from datetime import datetime
from flask import jsonify, make_response, request
from flask_restful import Resource, reqparse
from app.models.mission import Mission

requestArgsPost = reqparse.RequestParser() #definir os argumentos da solicitação HTTP
requestArgsPost.add_argument("name", type=str, help="Name of the mission", required=True)
requestArgsPost.add_argument("launch_date", type=str, help="Launch date of the mission (YYYY-MM-DD)", required=True)
requestArgsPost.add_argument("destination", type=str, help="Destination of the mission", required=True)
requestArgsPost.add_argument("status", type=str, help="Status of the mission", required=True)
requestArgsPost.add_argument("crew", type=str, help="Crew members of the mission", required=True)
requestArgsPost.add_argument("payload", type=str, help="Payload of the mission", required=True)
requestArgsPost.add_argument("duration", type=str, help="Duration of the mission", required=True)
requestArgsPost.add_argument("cost", type=float, help="Cost of the mission", required=True)
requestArgsPost.add_argument("status_description", type=str, help="Description of the mission status", required=True)

requestArgsUpdate = reqparse.RequestParser()
requestArgsUpdate.add_argument("id", type=str, help="Id of the mission")
requestArgsUpdate.add_argument("name", type=str, help="Name of the mission")
requestArgsUpdate.add_argument("launch_date", type=str, help="Launch date of the mission (DD/MM/YYYY)")
requestArgsUpdate.add_argument("destination", type=str, help="Destination of the mission")
requestArgsUpdate.add_argument("status", type=str, help="Status of the mission")
requestArgsUpdate.add_argument("crew", type=str, help="Crew members of the mission")
requestArgsUpdate.add_argument("payload", type=str, help="Payload of the mission")
requestArgsUpdate.add_argument("duration", type=str, help="Duration of the mission")
requestArgsUpdate.add_argument("cost", type=float, help="Cost of the mission")
requestArgsUpdate.add_argument("status_description", type=str, help="Description of the mission status")

requestArgsDelete = reqparse.RequestParser()
requestArgsDelete.add_argument("id", type=str, help="Id of the mission", required=True)


class MissionDetailView(Resource):
    def get(self, id):
        try:
            mission = Mission.getById(self, id)
            if (mission is None): 
                return make_response(jsonify(), 404)
            
            serialized_mission = {
                "id": mission.id,
                "name": mission.name,
                "launch_date": mission.launch_date.strftime("%Y-%m-%d"), 
                "destination": mission.destination,
                "status": mission.status,
                "crew": mission.crew,
                "payload": mission.payload,
                "duration": mission.duration.strftime("%Y-%m-%d %H:%M"),
                "cost": float(mission.cost),
                "status_description": mission.status_description
            }

            return make_response(jsonify({"mission": serialized_mission}), 200)
        except Exception as e:
            print("Ocorreu um error na listagem")
            print(e)
            return make_response(jsonify({"msg": "Internal Error"}), 500)

class MissionsView(Resource):
    def get(self):
        try:
            missions = []
            serialized_missions = []

            if (request.args.get("initialDate") is None or request.args.get("finalDate") is None):
                missions = Mission.list(self)
            else:
                initialDate = datetime.strptime(request.args.get("initialDate"), "%Y-%m-%d")
                finalDate = datetime.strptime(request.args.get("finalDate"), "%Y-%m-%d")
                missions = Mission.listByDate(self, initialDate, finalDate) or []
            
            for mission in missions:
                serialized_mission = {
                    "id": mission.id,
                    "name": mission.name,
                    "launch_date": mission.launch_date.strftime("%Y-%m-%d"), 
                    "duration": mission.duration.strftime("%Y-%m-%d %H:%M"), 
                    "destination": mission.destination,
                    "status": mission.status
                }
                serialized_missions.append(serialized_mission)

            return make_response(jsonify({"missions": serialized_missions}), 200)
        except ValueError as e:
            return make_response(jsonify({"msg": "Values not allowed"}), 400)
        except Exception as e:
            print("Ocorreu um error na listagem")
            print(e)
            return make_response(jsonify({"msg": "Internal Error"}), 500)


    def post(self):
        try:
            data = requestArgsPost.parse_args()
            launch_date = datetime.strptime(data["launch_date"], "%Y-%m-%d")
            duration = datetime.strptime(data["duration"], "%Y-%m-%d %H:%M")
            
            if (launch_date > duration):
                return make_response(jsonify({"msg": "Launch date must be earlier than duration"}), 400)

            Mission.save(self, data["name"], launch_date, data["destination"], data["status"], 
                                   data["crew"], data["payload"], duration, data["cost"], data["status_description"])

            return make_response(jsonify({"msg": "Mission create successfully!"}), 201)
        except Exception as e:
            print("Ocorreu um error")
            print(e)
            return make_response(jsonify({"msg": "Internal Error"}), 500)
    
    def put(self):
        try:
            data = requestArgsUpdate.parse_args()
            
            if (data["launch_date"] is not None):
                data["launch_date"] = datetime.strptime(data["launch_date"], "%Y-%m-%d")
            if (data["duration"] is not None):
                data["duration"] = datetime.strptime(data["duration"], "%Y-%m-%d %H:%M")

            # Pra remover os valores None do dicionario
            filtered = {k: v for k, v in data.items() if v is not None} 
            data.clear()
            data.update(filtered)

            Mission.update(self, data["id"], data)
            return make_response(jsonify({"msg": "Mission updated successfully!"}), 200)
        except Exception as e:
            print("Ocorreu um error ao atualizar a missão")
            print(e)
            return make_response(jsonify({"msg": "Internal Error"}), 500)


    def delete(self):
        try:
            data = requestArgsDelete.parse_args()
            Mission.remove(self, data["id"])
            return make_response(jsonify({"msg": "Mission deleted successfully!"}), 200)
        except Exception as e:
            print("Ocorreu um error ao deletar a missão")
            print(e)
            return make_response(jsonify({"msg": "Internal Error"}), 500)
