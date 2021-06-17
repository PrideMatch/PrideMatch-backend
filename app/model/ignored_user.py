from app import db

class IgnoredUser(db.Model):
    def __init__(self, id, user_id, ignored_user_id, number_of_ignores):
        self.id = id
        self.user_id = user_id
        self.ignored_user_id = ignored_user_id
        self.number_of_ignores = number_of_ignores

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    ignored_user_id = db.Column(db.String(50), nullable=False)
    number_of_ignores = db.Column(db.Integer, nullable=False)