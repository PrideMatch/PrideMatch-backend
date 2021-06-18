from sqlalchemy.orm import backref
from app import db

class User(db.Model):
    def __init__(self, id, username, email, display_orientation, display_gender, display_pronouns, password = '', gender = '', age = None, 
    profile_picture = None, orientation = '', about_me = '', pronouns='', interests = [], games = [], teammates = [], 
    added_users = [], ignored_users = [], socials=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.gender = gender
        self.age = age
        self.profile_picture = profile_picture
        self.orientation = orientation
        self.about_me = about_me
        self.pronouns = pronouns
        self.interests = interests
        self.socials = socials
        self.games = games
        self.teammates = teammates
        self.added_users = added_users
        self.ignored_users = ignored_users
        self.display_orientation = display_orientation
        self.display_gender = display_gender
        self.display_pronouns = display_pronouns
        

    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(35), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    profile_picture = db.Column(db.LargeBinary(), nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    orientation = db.Column(db.String(20), nullable=True)
    pronouns = db.Column(db.String(20), nullable=True)
    about_me = db.Column(db.String(255), nullable=True)
    display_orientation = db.Column(db.Boolean(), nullable=False)
    display_gender = db.Column(db.Boolean(), nullable=False)
    display_pronouns = db.Column(db.Boolean(), nullable=False)
    socials = db.relationship('Socials', uselist=False, backref='user', lazy=True)
    interests = db.relationship('Interest', backref='user', lazy=True)
    games = db.relationship('UserGame', backref='user', lazy=True)
    new_follows = db.relationship('UnreadFollow', backref='user', lazy=True)
    teammates = db.relationship('Teammate', lazy=True)
    added_users = db.relationship('AddedUser', lazy='noload')
    ignored_users = db.relationship('IgnoredUser', lazy='noload')