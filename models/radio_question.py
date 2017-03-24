from models.basicmodel import db


class RadioQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    cardinal = db.Column(db.Integer, nullable=False)
    question = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

    def __init__(self, content, cardinal, question):
        self.content = content
        self.cardinal = cardinal
        self.question = question

    def __repr__(self):
        return str(self.__dict__)
