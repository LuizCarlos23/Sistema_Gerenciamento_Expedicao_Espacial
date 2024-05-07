from app import db

class Missions(db.Model):
    __tablename__ = 'missions'
    __table_args__ = {'sqlite_autoincrement': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    launch_date = db.Column(db.Date)
    destination = db.Column(db.String(255))
    status = db.Column(db.String)
    crew = db.Column(db.String)
    payload = db.Column(db.String)
    duration = db.Column(db.String)
    cost = db.Column(db.Numeric)
    status_description = db.Column(db.Text)

    def __init__(self, name, launch_date, destination, status, crew, payload, duration, cost, status_description):
        self.name = name
        self.launch_date = launch_date
        self.destination = destination
        self.status = status
        self.crew = crew
        self.payload = payload
        self.duration = duration
        self.cost = cost
        self.status_description = status_description

    def save(self, name, launch_date, destination, status, crew, payload, duration, cost, status_description):
        try:
            add_banco = Missions(name, launch_date, destination, status, crew, payload, duration, cost, status_description)
            db.session.add(add_banco)
            db.session.commit()
        except Exception as e: 
            print(e)

    def update(self, id, **kwargs):
        try:
            db.session.query(Missions).filter(Missions.id==id).update(kwargs)
            db.session.commit()
        except Exception as e:
            print(e)

    def remove(self, id):
        try:
            db.session.query(Missions).filter(Missions.id==id).delete()
            db.session.commit()
        except Exception as e:
            print(e)
