from app import db

class Teammate(db.Model):
    def __init__(self, id, user_id, teammate_id):
        self.id = id
        self.user_id = id
        self.teammate_id = teammate_id
        
    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'))
    teammate_id = db.Column(db.String(50), nullable=False)