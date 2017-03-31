import datetime
import hashlib
import uuid

from models.basicmodel import db


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(50), index=True)
    name = db.Column(db.String(100), nullable=False)
    # owner is a reference to nia
    owner = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    confirmation = db.Column(db.Text, nullable=False)
    init_date = db.Column(db.Date, default=datetime.datetime.utcnow)

    def __init__(self, name, owner, description, confirmation, init_date=None):
        self.name = name
        self.owner = owner
        self.description = description
        self.confirmation = confirmation
        self.init_date = init_date
        self.code = self.generate_code()

    def __repr__(self):
        return str(self.__dict__)

    def generate_code(self):
        before_code = str(datetime.datetime.utcnow().strftime('%B%d%Y%H%M%S')) + str(self.owner) + str(uuid.uuid4().hex)
        return str(hashlib.sha256(before_code.encode('utf-8')).hexdigest())[:50]


