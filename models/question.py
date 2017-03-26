from models.basicmodel import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    cardinal = db.Column(db.Integer, nullable=False)
    required = db.Column(db.Boolean, default=True, nullable=False)
    survey = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)

    answers = db.relationship('Answer', backref='question', lazy='select')

    def __init__(self, title, subtitle, cardinal, required, survey):
        self.title = title
        self.subtitle = subtitle
        self.cardinal = cardinal
        self.required = required
        self.survey = survey

    def __repr__(self):
        return str(self.__dict__)
