from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app)

from app.models.mission import Mission
with app.app_context(): 
    db.create_all()

from app.views.missions_view import MissionsView, MissionDetailView
api.add_resource(MissionsView, "/missions")
api.add_resource(MissionDetailView, "/missions/<int:id>")