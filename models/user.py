from models.basicmodel import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=1)
    nick = db.Column(db.String(100), index=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Integer, nullable=False)

    def __init__(self, nick, email, password, name, surname, rol=0):
        self.nick = nick
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.rol = rol

    def __repr__(self):
        return self.nick
