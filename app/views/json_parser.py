from flask import json

def usergame_to_json(user_game):
    return json.dumps({'game_id': user_game.id})

def user_to_json(user):

    games = []
    teammates = []
    
    if user.games:
        for x in user.games:
            games.append(usergame_to_json(x))
    
    games_json = json.dumps(games)

    if user.socials:
        socials_json = socials_to_json(user.socials)

    if user.teammates:
        for x in user.teammates:
            teammates.append(teammate_to_json(x))

    teammates_json = json.dumps(teammates)

    return json.dumps({'id': user.id, 'username': user.username, 'email': user.email, 'gender': user.gender, 'age': user.age, 
    'orientation': user.orientation, 'about_me': user.about_me, 'socials': json.loads(socials_json), 'games': json.loads(games_json), 'teammates': json.loads(teammates_json)})
    
def teammate_to_json(teammate):
    return json.dumps({'teammate_id': teammate.teammate_id})

def socials_to_json(socials):
    return json.dumps({'facebook': socials.facebook, 'instagram': socials.instagram,
    'twitter': socials.twitter, 'discord_id': socials.discord_id})