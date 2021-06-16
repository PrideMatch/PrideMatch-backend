from app import db

class Socials(db.Model):
    def __init__(self, id, user_id, facebook, instagram, twitter, discord_id):
        self.id = id
        self.user_id = user_id
        self.facebook = facebook
        self.instagram = instagram
        self.twitter = twitter 
        self.discord_id = discord_id

    id = db.Column(db.String(50), primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    facebook = db.Column(db.String(100), nullable=True)
    instagram = db.Column(db.String(100), nullable=True)
    twitter = db.Column(db.String(100), nullable=True)
    discord_id = db.Column(db.String(20), nullable=True)