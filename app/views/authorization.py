import server_secrets
import jwt
from functools import wraps
from flask import jsonify, request
from google.auth.transport import requests
from google.oauth2 import id_token
from app.model import User
from flask.helpers import make_response


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message' : 'Token is missing'}), 403
        
        google_token = False
        jwt_token = False

        try:
            id_token.veriify_oauth2_token(token, requests.Request(), server_secrets.CLIENT_ID)
            google_token = True
        except:
            pass

        try:
            data=jwt.decode(token, server_secrets.SECRET_KEY,algorithms=["HS256"])
            user = User.query.filter_by(id=data['id']).first()
            jwt_token = True
        except:
            pass

        if(not google_token and not jwt_token):
             return jsonify({'message' : 'Token is invalid'}), 403

        return f(*args, **kwargs)
    
    return decorated

def verify_user_id(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message' : 'Token is missing'}), 403

        try:
            data=jwt.decode(token, server_secrets.SECRET_KEY,algorithms=["HS256"])
            user_id = request.args.get('user_id')
            if token['id'] != user_id:
                return make_response('Unauthorized', 401)
        except:
            pass

        return f(*args, **kwargs)
    return decorated
