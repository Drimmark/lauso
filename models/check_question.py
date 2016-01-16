from models.basicmodel import db

class Check_question(db.Model):

    def __init__(self):
        pass

    def __repr__(self):
        return self.content
