from app import db

class UnreadFollow(db.Model):
    def __init__(self, id, followed_by):
        self.id = id
        self.followed_by = followed_by

    id = db.Column(db.String(50), primary_key=True)
    followed_by = db.Column(db.String(50), db.ForeignKey('user.id'))
    teammates = db.Column(db.Boolean(), nullable=False)