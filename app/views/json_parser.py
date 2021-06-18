from flask import json

def usergame_to_json(user_game):
    if user_game.game:
        return user_game.game
    else:
        return "null"

def interest_to_json(interest):
    if interest.interest:
        return interest.interest
    else:
        return "null"

def user_to_json(user):

    games = []
    teammates = []
    interests = []
    new_follows = []

    if user.socials:
        socials_json = socials_to_json(user.socials)

    if user.teammates:
        for x in user.teammates:
            teammates.append(teammate_to_json(x))

    teammates_json = json.dumps(teammates)

    if user.interests:
        for i in user.interests:
            interests.append(interest_to_json(i))

    interests_json = json.dumps(interests)

    if user.new_follows:
        for f in user.new_follows:
            new_follows.append(unreadfollow_to_json(f))

    new_follows_json = json.dumps(new_follows)

    if user.games:
        for x in user.games:
            games.append(usergame_to_json(x))
    
    games_json = json.dumps(games)
        
    pronouns = ''
    if user.display_pronouns:
        pronouns = user.pronouns
    
    gender = ''
    if user.display_gender:
        gender = user.gender
    
    orientation = ''
    if user.display_orientation:
        orientation = user.orientation

    return json.dumps({'id': user.id, 'username': user.username, 'email': user.email, 'gender': gender, 'age': user.age, 
    'orientation': orientation, 'pronouns': pronouns, 'about_me': user.about_me, 'socials': json.loads(socials_json), 
    'games': json.loads(games_json), 'teammates': json.loads(teammates_json), 'interests': json.loads(interests_json), 'new_follows': json.loads(new_follows_json)})
    
def teammate_to_json(teammate):
    if teammate.teammate_id:
        return teammate.teammate_id
    else:
        return "null"

def socials_to_json(socials):

    if socials.facebook:
        facebook = socials.facebook
    else:
        facebook = "null"

    if socials.instagram:
        instagram = socials.instagram
    else:
        instagram = "null"

    if socials.twitter:
        twitter = socials.twitter
    else:
        twitter = "null"

    if socials.discord_id:
        discord_id = socials.discord_id
    else:
        discord_id = "null"

    return json.dumps({'facebook': facebook, 'instagram': instagram,
    'twitter': twitter, 'discord_id': discord_id})

def forumcomment_to_json(comment):

    if comment.reply_to:
        reply_to = comment.reply_to
    else:
        reply_to = "null"

    return json.dumps({'id': comment.id, 'text': comment.text, 'creation_time': comment.creation_time, 'author': comment.author, 
    'thread': comment.thread, 'reply_to': reply_to})

def forumthread_to_json(thread):
    comments = []

    if thread.comments:
        for c in thread.comments:
            comments.append(forumcomment_to_json(c))

    comments_json = json.dumps(comments)

    return json.dumps({'id': thread.id, 'author': thread.author, 'title': thread.title, 'creation_time': thread.creation_time,
    'text': thread.text, 'forum_section': thread.forum_section, 'comments': json.loads(comments_json)})

def unreadfollow_to_json(follow):
    return json.dumps({'id': follow.id, 'followed_by': follow.followed_by, 'teammates': follow.teammates})