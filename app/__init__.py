from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app)

from app.models.mission import Missions as MissionModel
with app.app_context(): 
    db.create_all()

from app.views.missions_view import MissionsView
api.add_resource(MissionsView, "/missions")