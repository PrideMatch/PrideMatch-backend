from app import db

class ForumComment(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    text = db.Column(db.Text, nullable=False)
    creation_time = db.Column(db.DateTime(), nullable=False)
    author = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    thread = db.Column(db.String(50), db.ForeignKey('forumthread.id'), nullable=False)
    reply_to = db.Column(db.String(50), db.ForeignKey('forumcomment.id'), nullable=True)
    
    