from app import db

class Interest(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    interest=db.Column(db.String(25), nullable=False)