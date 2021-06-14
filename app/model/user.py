from app import db

class User(db.Model):
    def __init__(self, id, username, password, email, socials, games, gender = None, age = None, profile_picture = None, orientation = None, about_me = None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.gender = gender
        self.age = age
        self.profile_picture = profile_picture
        self.orientation = orientation
        self.about_me = about_me
        self.socials = socials
        self.games = games
        

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(35), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    gender = db.Column(db.String(20), nullable=True)
    age = db.Column(db.Integer(), nullable=True)
    profile_picture = db.Column(db.LargeBinary(), nullable=True)
    orientation = db.Column(db.String(20), nullable=True)
    about_me = db.Column(db.String(150), nullable=True)
    games = db.Column(db.String(255), nullable=False)
    socials = db.relationship('Socials', backref='user', lazy=True)


