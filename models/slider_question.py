from models.basicmodel import db


class SliderQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    cardinal = db.Column(db.Integer, nullable=False)
    start_value = db.Column(db.Integer, nullable=False)
    end_value = db.Column(db.Integer, nullable=False)
    survey = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
    required = db.Column(db.Boolean, default=True)
    start_text = db.Column(db.String(100))
    end_text = db.Column(db.String(100))

    answers = db.relationship('SliderAnswer', backref='box_question', lazy='select')

    def __init__(self, title, subtitle, cardinal, survey, required=None, radio=None):
        self.title = title
        self.subtitle = subtitle
        self.cardinal = cardinal
        self.survey = survey
        self.required = required
        self.radio = radio

    def __repr__(self):
        return str(self.__dict__)
