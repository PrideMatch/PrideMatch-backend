import uuid
from app import app, db
from app.views.authorization import token_required
from flask import jsonify, request
from flask.helpers import make_response
from app.model import User, AddedUser, Teammate

@app.route('/recommendations/follow/', methods=['POST'])
@token_required
def follow():
    user_id = request.args.get('user_id')
    data = request.get_json()
    followed_user = data.get('added_user_id')

    if not user_id or not data or not followed_user:
        make_response('Bad request', 400)

    added_user = AddedUser(id=str(uuid.uuid4()), user_id=user_id, followed_user_id=followed_user)
    
    db.session.add(added_user)
    db.session.commit()

    return make_response('User followed', 200)
    

