from models.basicmodel import db

class Check_answer(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = 1)
	answer = db.Column(db.Integer, db.ForeignKey('check_question_id'), nullable = False, index = True)
	owner = db.Column(db.Integer, db.ForeignKey('user_id'), nullable = False, index = True)

    def __init__(self):
        self.id = id
        self.answer = answer
        self.owner = owner

    def __repr__(self):
        return self.id
