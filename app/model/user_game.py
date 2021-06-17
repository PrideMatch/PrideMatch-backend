from app import db

class UserGame(db.Model):
    def __init__(self, id, user_id, game):
        self.id = id
        self.user_id = user_id
        self.game = game
        
    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'))
    game = db.Column(db.String(50), nullable=False)
