from models.basicmodel import db


class RadioAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False, index=True)
    answer = db.Column(db.Integer, db.ForeignKey('radio_question.id'), nullable=False)
    owner = db.Column(db.Integer, nullable=False)

    def __init__(self, question, answer, owner):
        self.question = question
        self.answer = answer
        self.owner = owner

    def __repr__(self):
        return str(self.__dict__)
