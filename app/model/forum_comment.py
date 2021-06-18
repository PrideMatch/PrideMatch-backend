from app import db

class ForumComment(db.Model):
    def __init__(self, id, text, creation_time, author, thread, reply_to=''):
        self.id=id
        self.author=author
        self.text=text
        self.creation_time=creation_time
        self.thread=thread
        self.reply_to=reply_to
        
    id = db.Column(db.String(50), primary_key=True)
    text = db.Column(db.Text, nullable=False)
    creation_time = db.Column(db.DateTime(), nullable=False)
    author = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    thread = db.Column(db.String(50), db.ForeignKey('forumthread.id'), nullable=False)
    reply_to = db.Column(db.String(50), db.ForeignKey('forumcomment.id'), nullable=True)
    
    