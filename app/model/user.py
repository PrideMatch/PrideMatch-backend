from app import db

class User(db.Model):
    def __init__(self, id, username, email, socials, password = None, gender = None, age = None, 
    profile_picture = None, orientation = None, about_me = None, games = None, teammates = None, added_users = None):
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
        

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(35), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    profile_picture = db.Column(db.LargeBinary(), nullable=True)
    orientation = db.Column(db.String(20), nullable=True)
    about_me = db.Column(db.String(255), nullable=True)
    socials = db.relationship('Socials', backref='user', lazy=True)
    games = db.relationship('UserGames', backref='user', lazy=True)
    teammates = db.relationship('Teammates', lazy=True)
    added_users = db.relationship('AddedUsers', lazy='noload')


