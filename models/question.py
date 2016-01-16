from models.basicmodel import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=1)
    cardinal = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    required = db.Column(db.Boolean, default=True, nullable=False)
    survey = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)

    def __init__(self, id, cardinal, content, required, survey):
        self.id = id
        self.cardinal = cardinal
        self.content = content
        self.required = required
        self.survey = survey


    def __repr__(self):
        return self.content
