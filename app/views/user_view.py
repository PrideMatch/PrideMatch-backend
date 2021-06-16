import secrets
from app.model.user import User
from flask.helpers import make_response
from app import app
from app.views.authorization import token_required
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

@app.route('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return make_response('Invalid request', 400)
    
    user = User.query.filter_by(name=username).first()

    if not user:
        return make_response('Invalid username or password', 400)

    if  check_password_hash(user.password, password):
        token = jwt.encode({'id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=2)}, secrets.SECRET_KEY)
        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Invalid username or password', 401)