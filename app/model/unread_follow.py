from app import db

class UnreadFollow(db.Model):
    def __init__(self, id, user_id, followed_by, teammates):
        self.id = id
        self.user_id = user_id
        self.followed_by = followed_by
        self.teammates = teammates

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    followed_by = db.Column(db.String(50), nullable=False)
    teammates = db.Column(db.Boolean(), nullable=False)