from models.basicmodel import db

class Answer(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = 1)
	content = db.Column(db.Text, nullable = False)
	question = db.Column(db.Integer, db.ForeignKey('question.id'), nullable = False)
	owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self):
        self.id = id
        self.content = content
        self.question = question
        self.owner = owner

    def __repr__(self):
        return self.content
