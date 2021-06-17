from app import db

class ForumThread(db.Model):
    def __init__(self, id, author, title, creation_time, text, forum_section ='', comments=[]):
        self.id=id
        self.author=author
        self.title=title
        self.creation_time=creation_time
        self.text=text
        self.forum_section=forum_section
        self.comments=comments

    id = db.Column(db.String(50), primary_key=True)
    author = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    creation_time = db.Column(db.DateTime(), nullable=False)
    text = db.Column(db.Text, nullable=False)
    forum_section = db.Column(db.String(40), nullable=True)
    comments = db.relationship('ForumComment', backref='forumthread', lazy=True)
