from models.basicmodel import db


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.Integer, db.ForeignKey('box_question.id'), nullable=False)
    name = db.Column(db.Text, nullable=False)

    def __init__(self, question, name):
        self.question = question
        self.name = name

    def __repr__(self):
        return str(self.__dict__)
