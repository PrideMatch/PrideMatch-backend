from app import db

class User(db.Model):
    def __init__(self, id, username, email, socials, password = '', gender = '', age = None, 
    profile_picture = None, orientation = '', about_me = '', games = [], teammates = [], added_users = []):
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
        self.teammates = teammates
        self.added_users = added_users
        

    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(35), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    profile_picture = db.Column(db.LargeBinary(), nullable=True)
    orientation = db.Column(db.String(20), nullable=True)
    about_me = db.Column(db.String(255), nullable=True)
    socials = db.relationship('Socials', uselist=False, backref='user', lazy=True)
    games = db.relationship('UserGame', backref='user', lazy=True)
    teammates = db.relationship('Teammate', lazy=True)
    added_users = db.relationship('AddedUser', lazy='noload')