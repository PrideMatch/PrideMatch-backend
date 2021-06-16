import datetime
import uuid
import jwt
import server_secrets
from app import app, db
from app.model import Socials, User
from flask import jsonify, request
from flask.helpers import make_response
from werkzeug.security import check_password_hash, generate_password_hash


@app.route('/login', methods=['GET'])
def login():
    username = request.json['username']
    password = request.json['password']

    if not username or not password:
        return make_response('Invalid request', 400)
    
    user = User.query.filter_by(username=username).first()

    if not user:
        return make_response('Invalid username or password', 400)

    if  check_password_hash(user.password, password):
        token = jwt.encode({'id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1)}, server_secrets.SECRET_KEY)
        return jsonify({'token' : token})

    return make_response('Invalid username or password', 401)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    hashed_pass = generate_password_hash(data['password'], method='sha256')

    s_json = data['socials']
    socials = Socials(id=s_json['id'], user_id=s_json['user_id'], facebook=s_json['facebook'], instagram=s_json['instagram'], 
    twitter=s_json['twitter'], discord_id=s_json['discord_id'])

    user = User(id=str(uuid.uuid4()), username=data['username'], email=data['email'], password=hashed_pass,
     gender=data['gender'], age=data['age'], profile_picture=data['profile_picture'], orientation=data['orientation'],
     about_me=data['about_me'], socials=socials)
    
    db.session.add(user)
    db.session.commit()

    return make_response('User created', 201)

