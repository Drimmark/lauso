from models.basicmodel import db

class Survey(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=1)
	code = db.Column(db.String(50), index=True)
	name = db.Column(db.String(100), nullable = False)
	owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) #Add reference
	description = db.Column(db.Text, nullable = False)
	confirmation = db.Column(db.Text, nullable = False)
	init_date = db.Column(db.date, nullable = False)

    def __init__(self):
        self.id = id
        self.code = code
        self.name = name
        self.owner = owner
        self.description = description
        self.confirmation = confirmation
        self.init_date = init_date

    def __repr__(self):
        return self.name
