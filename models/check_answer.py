from models.basicmodel import db


class CheckAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answer = db.Column(db.Integer, db.ForeignKey('check_question_id'), nullable=False, index=True)
    owner = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)

    def __init__(self, answer, owner):
        self.answer = answer
        self.owner = owner

    def __repr__(self):
        return self.id
