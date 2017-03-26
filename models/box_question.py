from models.basicmodel import db


class BoxQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    cardinal = db.Column(db.Integer, nullable=False)
    survey = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
    required = db.Column(db.Boolean, default=True)
    radio = db.Column(db.Boolean, default=False)

    options = db.relationship('Option', backref='box_question', lazy='select')
    answers = db.relationship('BoxAnswer', backref='box_question', lazy='select')

    def __init__(self, title, subtitle, cardinal, survey, required=None, radio=None):
        self.title = title
        self.subtitle = subtitle
        self.cardinal = cardinal
        self.survey = survey
        self.required = required
        self.radio = radio

    def __repr__(self):
        return str(self.__dict__)
