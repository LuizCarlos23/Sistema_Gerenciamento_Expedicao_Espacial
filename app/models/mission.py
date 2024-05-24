from app import db

class Mission(db.Model):
    __tablename__ = 'missions'
    __table_args__ = {'sqlite_autoincrement': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    launch_date = db.Column(db.Date)
    destination = db.Column(db.String(255))
    status = db.Column(db.String)
    crew = db.Column(db.String)
    payload = db.Column(db.String)
    duration = db.Column(db.DateTime)
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

    def getById(self, id):
        try:
            mission = db.session.query(Mission).filter(Mission.id==id).first()
            return mission
        except Exception as e:
            print(e)


    def list(self):
        try:
            missions = db.session.query(Mission).order_by(Mission.launch_date.desc()).all()
            return missions
        except Exception as e:
            print(e)
        
    def listByDate(self, initialDate, finalDate):
        try:
            missions = db.session.query(Mission).filter((Mission.launch_date >= initialDate) & (Mission.launch_date <= finalDate)).order_by(Mission.launch_date.desc()).all()
            return missions
        except Exception as e:
            print(e)

    def save(self, name, launch_date, destination, status, crew, payload, duration, cost, status_description):
        try:
            add_banco = Mission(name, launch_date, destination, status, crew, payload, duration, cost, status_description)
            db.session.add(add_banco)
            db.session.commit()
        except Exception as e: 
            print(e)

    def update(self, id, updated_data = {}):
        try:
            db.session.query(Mission).filter(Mission.id==id).update(updated_data)
            db.session.commit()
        except Exception as e:
            print(e)

    def remove(self, id):
        try:
            db.session.query(Mission).filter(Mission.id==id).delete()
            db.session.commit()
        except Exception as e:
            print(e)