from datetime import datetime
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from app.models.mission import Missions

requestArgsPost = reqparse.RequestParser() #definir os argumentos da solicitação HTTP
requestArgsPost.add_argument('name', type=str, help='Name of the mission', required=True)
requestArgsPost.add_argument('launch_date', type=str, help='Launch date of the mission (YYYY-MM-DD)', required=True)
requestArgsPost.add_argument('destination', type=str, help='Destination of the mission', required=True)
requestArgsPost.add_argument('status', type=str, help='Status of the mission', required=True)
requestArgsPost.add_argument('crew', type=str, help='Crew members of the mission', required=True)
requestArgsPost.add_argument('payload', type=str, help='Payload of the mission', required=True)
requestArgsPost.add_argument('duration', type=str, help='Duration of the mission', required=True)
requestArgsPost.add_argument('cost', type=float, help='Cost of the mission', required=True)
requestArgsPost.add_argument('status_description', type=str, help='Description of the mission status', required=True)

class MissionsView(Resource):
    def get(self):
        return jsonify("All missions")
    
    def post(self):
        try:
            datas = requestArgsPost.parse_args()
            print(datas)
            datetime_str = datas['launch_date']
            launch_date = datetime.strptime(datetime_str, '%d/%m/%Y')
            Missions.save(self, datas['name'], launch_date, datas['destination'], datas['status'], 
                                   datas['crew'], datas['payload'], datas['duration'], datas['cost'], datas['status_description'])

            return make_response(jsonify({"message": 'Mission create successfully!'}), 201)
        except Exception as e:
            print("Ocorreu um error")
            print(e)
            return make_response(jsonify({'status': 500, 'msg': "Internal Error"}), 500)
    
    def update(self):
        return jsonify("Edite mission")

    def delete(self):
        return jsonify("Delete mission")
    