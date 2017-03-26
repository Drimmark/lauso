from models.basicmodel import db


class SliderAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.Integer, db.ForeignKey('slider_question.id'), nullable=False)
    select_option = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.Integer, nullable=False)

    def __init__(self, question, select_option, owner):
        self.question = question
        self.select_option = select_option
        self.owner = owner

    def __repr__(self):
        return str(self.__dict__)
