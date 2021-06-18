import uuid
from app import app, db
from app.model import ForumThread, ForumComment
from flask.helpers import make_response
from flask import json, jsonify, request
from app.views.json_parser import forumthread_to_json, forumcomment_to_json
from app.views.authorization import token_required

@app.route('/forum/threads', methods=['GET'])
@token_required
def get_threads_from_section():
    section_name = request.args.get('forum_section')

    if not section_name:
        return make_response("Bad request", 400)

    forum_threads = ForumThread.query.filter_by(forum_section=section_name).limit(20).all()
    forum_threads = sorted(forum_threads, key=compare_items_by_date)

    forum_threads_json = []

    for thread in forum_threads:
        forum_threads_json.append(forum_threads_json(thread))

    return make_response(jsonify(forum_threads_json), 200)

@app.route('/forum/threads', methods=['POST'])
@token_required
def add_thread_to_section():
    section_name = request.args.get('forum_section')
    data = request.get_json()

    if not section_name or not data:
        return make_response("Bad request", 400)
    
    forum_thread = ForumThread(id=str(uuid.uuid4()), author=data.get('author'), title=data.get('title'), creation_time=data.get('creation_time'),
    text=data.get('text'), forum_section=section_name)

    db.session.add(forum_thread)
    db.session.commit()

    return make_response('Forum thread created', 201)

@app.route('/forum/threads', methods=['DELETE'])
@token_required
def remove_thread():
    thread_id = request.args.get('thread_id')

    if not thread_id:
        return make_response("Bad request", 400)

    thread = ForumThread.query.filter_by(id=thread_id).first()
    db.session.delete(thread)
    db.session.commit()

    return make_response('Forum thread removed', 200)

@app.route('/forum/comments', methods=['GET'])
@token_required
def get_comments_from_thread():
    thread_id = request.args.get('thread_id')

    if not thread_id:
        return make_response("Bad request", 400)

    comments = ForumComment.query.filter_by(thread=thread_id).all()
    comments = sorted(comments, key=compare_items_by_date, reverse=True)

    comments_json = []

    for comment in comments:
        comments_json.append(forumcomment_to_json(comment))

    return make_response(jsonify(comments_json), 200)

@app.route('/forum/comments', methods=['POST'])
@token_required
def add_comment_on_thread():
    thread_id=request.args.get('thread_id')
    data = request.get_json()

    if not thread_id or not data:
        return make_response('Bad Request', 400)

    comment = ForumComment(id=str(uuid.uuid4()), text=data.get('text'), creation_time=data.get('creation_time'), author=data.get('author'), 
    thread=data.get('thread'), reply_to=data.get('reply_to'))

    db.session.add(comment)
    db.session.commit()

    return make_response('Comment added', 201)

@app.route('/forum/comments', methods=['DELETE'])
@token_required
def remove_comment():
    comment_id=request.args.get('comment_id')

    if not comment_id:
        return make_response('Bad Request', 400)

    comment = ForumComment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()

    return make_response('Comment removed', 200)

def compare_items_by_date(item1, item2):
    if item1.creation_time < item2.creation_time:
        return -1
    elif item1.creation_time > item2.creation_time:
        return 1
    else:
        return 0