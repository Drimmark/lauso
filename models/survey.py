import datetime

from models.basicmodel import db


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(50), nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    # owner is a reference to nia
    owner = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    confirmation = db.Column(db.Text, nullable=False)
    init_date = db.Column(db.Date, default=datetime.datetime.utcnow)

    def __init__(self, code, name, owner, description, confirmation, init_date=None):
        self.code = code
        self.name = name
        self.owner = owner
        self.description = description
        self.confirmation = confirmation
        self.init_date = init_date

    def __repr__(self):
        return str(self.__dict__)
