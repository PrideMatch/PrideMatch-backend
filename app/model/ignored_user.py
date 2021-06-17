from app import db

class IgnoredUser(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'))
    ignored_user_id = db.Column(db.String(50), db.ForeignKey('user.id'))