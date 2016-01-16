from models.basicmodel import db

class Radio_answer(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = 1)
	question = dbColumn(db.Integer, db.ForeignKey('question.id'), nullable = False, index = True)
	answer = dbColumn(db.Integer, db.ForeignKey('radio_question.id'), nullable = False)
	owner = dbColumn(db.Integer, db.ForeignKey('user_id'), index = True)

    def __init__(self):
        self.id = id
        self.question = question
        self.answer = answer
        self.owner = owner

    def __repr__(self):
        return self.id
