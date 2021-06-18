from app import app, db
from app.model import ForumThread
from flask.helpers import make_response
from flask import json, jsonify, request
from app.views.json_parser import user_to_json
from app.views.authorization import token_required

@app.route('/forum/threads')
@token_required
def get_threads_from_section():
    section_name = request.args.get('forum_section')

    if not section_name:
        return make_response("Bad request", 400)

    forum_threads = ForumThread.query.filter_by(forum_section=section_name).limit(20).all()
    forum_threads = sorted(forum_threads, key=compare_items_by_date)

    return make_response(jsonify(forum_threads), 200)

def compare_items_by_date(item1, item2):
    if item1.creation_time < item2.creation_time:
        return -1
    elif item1.creation_time > item2.creation_time:
        return 1
    else:
        return 0

