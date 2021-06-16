from app import db

class AddedUser(db.Model):
    def __init__(self, id, user_id, followed_user_id):
        self.id = id
        self.user_id = user_id
        self.followed_user_id = followed_user_id

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    followed_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))