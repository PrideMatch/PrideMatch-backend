import datetime
import uuid
import jwt
import server_secrets
import os
from app import app, db
from app.model import Socials, User, Interest, UserGame, interest
from flask import json, jsonify, request, send_file
from flask.helpers import make_response
from werkzeug.security import check_password_hash, generate_password_hash
from app.views.json_parser import user_to_json
from app.views.authorization import token_required, verify_user_id
from io import BytesIO
from PIL import Image

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

    user_id = str(uuid.uuid4())

    hashed_pass = ''
    if data.get('password'):
        hashed_pass = generate_password_hash(data.get('password'), method='sha256')

    s_json = data.get('socials')
    interests_json = data.get('interests')
    games_json = data.get('games')

    if s_json and interests_json and games_json:
        socials = Socials(id=str(uuid.uuid4()), user_id=user_id, facebook=s_json.get('facebook'), instagram=s_json.get('instagram'), 
        twitter=s_json.get('twitter'), discord_id=s_json.get('discord_id'))

        db.session.add(socials)

        for i in json.loads(interests_json):
            interest = Interest(id=str(uuid.uuid4()), user_id=user_id, interest=i)
            db.session.add(interest)

        for g in json.loads(games_json):
            game = UserGame(id=g, user_id=user_id)
            db.session.add(game)
    else:
        return make_response("Bad request", 400)

    user = User(id=str(uuid.uuid4()), username=data.get('username'), email=data.get('email'), password=hashed_pass,
     gender=data.get('gender'), pronouns=data.get('pronouns'), age=data.get('age'), orientation=data.get('orientation'),
     about_me=data.get('about_me'), display_pronouns=data.get('display_pronouns'), display_gender=data.get('display_gender'), display_orientation=data.get('display_orientation'))
    
    db.session.add(user)
    db.session.commit()

    return make_response('User created', 201)

@app.route('/user', methods=['GET'])
@token_required
def get_user():
    user_id = request.args.get('user_id')
    token = request.headers.get('Authorization')

    user = User.query.filter_by(id=user_id).first()
    
    if token['id'] != user_id:
        user.teammates = []
        user.new_follows = []

    return make_response(user_to_json(user), 200)

@app.route('/user', methods=['PUT'])
@token_required
@verify_user_id
def update_user():
    user_id = request.args.get('user_id')
    data = request.get_json()

    s_json = data.get('socials')

    if not user_id or not s_json:
        return make_response("Bad request", 400)
    
    socials = Socials.query.filter_by(user_id=user_id).first()
    user = User.query.filter_by(id=user_id).first()

    if not user and not socials:
        return make_response("Bad request", 400)
    
    # update socials
    socials.facebook = s_json.get('facebook')
    socials.instagram = s_json.get('instagram')
    socials.twitter = s_json.get('twitter')
    socials.discord_id = s_json.get('discord_id')

    # update user data
    user.username = data.get('username')
    user.email = data.get('email')
    if data.get('password'):
        user.password = generate_password_hash(data.get('password'), method='sha256')
    user.gender = data.get('gender')
    user.age = data.get('age')
    user.orientation=data.get('orientation')
    user.pronouns=data.get('pronouns')
    user.about_me=data.get('about_me')
    user.display_pronouns=data.get('display_pronouns')
    user.display_gender=data.get('display_gender')
    user.display_orientation=data.get('display_orientation')

    db.session.commit()

    return make_response("User updated", 200)

@app.route('/user', methods=['DELETE'])
@token_required
@verify_user_id
def delete_user():
    user_id = request.args.get('user_id') 

    if not user_id:
        return make_response("Bad request", 400)
    
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return make_response("Bad request", 400)

    db.session.delete(user)
    db.session.commit()

    return make_response("User removed", 200)

@app.route('/interest', methods=['POST'])
@token_required
@verify_user_id
def add_interest():
    user_id = request.args.get('user_id')
    data = request.get_json()

    if not user_id and not data:
        return make_response("Bad request", 400)

    interests_models = Interest.query.filter_by(user_id=user_id).all()

    interests = []

    if interests_models:
        for i in interests_models:
            interests.append(i.interest)

    if data.get('interest') not in interests:
        interest = Interest(id=str(uuid.uuid4()), user_id=user_id, interest=data.get('interest'))
        db.session.add(interest)
        db.session.commit()
        return make_response('Interest added', 201)

    return make_response('Intrest already exists', 409)

@app.route('/interest', methods=['DELETE'])
@token_required
@verify_user_id
def remove_interest():
    user_id = request.args.get('user_id')
    data = request.get_json()

    if not user_id and not data:
        return make_response("Bad request", 400)

    interests_models = Interest.query.filter_by(user_id=user_id).all()

    interests = []

    if interests_models:
        for i in interests_models:
            interests.append(i.interest)

    if data.get('interest') in interests:
        interest = Interest.query.filter_by(user_id=user_id, interest=data.get('interest')).first()
        db.session.delete(interest)
        db.session.commit()
        return make_response('Interest removed', 200)

    return make_response('Interest doesnt exist', 404)

@app.route('/usergame', methods=['POST'])
@token_required
@verify_user_id
def add_usergame():
    user_id = request.args.get('user_id')
    data = request.get_json()

    if not user_id and not data:
        return make_response("Bad request", 400)

    user_games_models = UserGame.query.filter_by(user_id=user_id).all()

    games = []

    if user_games_models:
        for g in user_games_models:
            games.append(g.game)

    if data.get('game') not in games:
        user_game = UserGame(id=str(uuid.uuid4()), user_id=user_id, game=data.get('game'))
        db.session.add(user_game)
        db.session.commit()
        return make_response('Game added', 201)

    return make_response('Game is already added', 409)

@app.route('/usergame', methods=['DELETE'])
@token_required
@verify_user_id
def remove_usergame():
    user_id = request.args.get('user_id')

    data = request.get_json()

    if not user_id and not data:
        return make_response("Bad request", 400)

    user_games_models = UserGame.query.filter_by(user_id=user_id).all()

    games = []

    if user_games_models:
        for g in user_games_models:
            games.append(g.game)
    
    if data.get('game') in games:
        user_game = UserGame.query.filter_by(user_id=user_id, game=data.game('game')).first()
        db.session.delete(user_game)
        db.session.commit()
        return make_response('Game removed', 200)

    return make_response('Game is not on the list', 404)

@app.route('/user/profile_pic', methods=['GET'])
@token_required
@verify_user_id
def get_profile_picture():
    user_id = request.args.get('user_id')

    if not user_id:
        return make_response("Bad request", 400)
    
    user = User.query.get_or_404(user_id)
    picture = BytesIO(user.profile_picture)

    if not picture:
        return make_response("Picture not found", 404)
    
    return send_file(picture, attachment_filename='profile_pic', as_attachment=True)

@app.route('/user/profile_pic', methods=['POST'])
@token_required
@verify_user_id
def add_profile_picture():
    user_id = request.args.get('user_id')
    file = request.get_data()

    if not user_id or not file:
        return make_response("Bad request", 400)

    user = User.query.get_or_404(user_id)

    image = Image.open(BytesIO(file))
    image = image.resize((300,300),Image.ANTIALIAS)
    image.save('image.jpg',quality=50,optimize=True)
    im = open("image.jpg", "rb") 
    user.profile_picture = im.read()
    db.session.commit()
    im.close()
    os.remove("image.jpg")

    return make_response('Profile picture added', 201)

@app.route('/user/profile_pic', methods=['DELETE'])
@token_required
@verify_user_id
def remove_profile_picture():
    user_id = request.args.get('user_id')

    if not user_id:
        return make_response("Bad request", 400)

    user = User.query.get_or_404(user_id)

    user.profile_picture=None
    db.session.commit()

    return make_response('Profile picture removed', 200)

@app.route('/user/profile_pic', methods=['PUT'])
@token_required
@verify_user_id
def update_profile_picture():
    user_id = request.args.get('user_id')

    if not user_id:
        return make_response("Bad request", 400)

    user = User.query.get_or_404(user_id)

    user.profile_picture=None
    db.session.commit()

    return make_response('Profile picture updated', 200)
