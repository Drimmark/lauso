from models.basicmodel import db

class Survey(db.Model):
	survey_id = db.Column(db.Integer, primary_key=True, autoincrement=1)
	code = db.Column(db.String(50), index=True)
	name = db.Column(db.String(100), nullable = False)
	owner = db.Column(db.Integer, nullable = False) #Add reference
	description = db.Column(db.Text, nullable = False)
	init_date = db.Column(db.date, nullable = False)

    def __init__(self):
        pass

    def __repr__(self):
        pass
