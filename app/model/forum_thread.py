from app import db

class ForumThread(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    author = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    creation_time = db.Column(db.DateTime(), nullable=False)
    text = db.Column(db.Text, nullable=False)
    forum_section = db.Column(db.String(40), nullable=True)
    comments = db.relationship('ForumComment', backref='forumthread', lazy=True)
