from app import db

class UserGame(db.Model):
    def __init__(self, id, user_id):
        self.id = id
        self.user_id = user_id
        
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
