from models.basicmodel import db


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    question = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    owner = db.Column(db.Integer, nullable=False)

    def __init__(self, content, question, owner):
        self.content = content
        self.question = question
        self.owner = owner

    def __repr__(self):
        return str(self.__dict__)
