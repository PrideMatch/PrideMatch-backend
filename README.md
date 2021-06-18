# Endpoints

# User

### Login

Use this endpoint to get access token.

REQUEST:

```jsx
GET url/login
```

BODY (JSON):

```jsx
{
	"username": "name",
	"password": "password"
}
```

RESPONSES:

**SUCCESSFUL:**

STATUS CODE: 200 OK

```jsx
{
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjI1ODI1OTcxLTAyNjMtNGY5Yy1hZjlmLWM5ZDQ5YTc4ZjcwYyIsImV4cCI6MTYyMzk2ODczN30.eTQVjLAw_FGiyqQXOSp5n3ft_fzFvSYrxr6y8ZO_Xkk"
}

```

### Register

Use this endpoint to add user

REQUEST:

```jsx
POST url/register
```

BODY:

```jsx
{
    "username": "name",
    "password": "password123",
    "email": "name@gmail.com",
    "gender": "female",
    "age": 20,
    "orientation": "heterosexual",
		"pronouns": "she/her",
    "about_me": "Lorem ipsum or whatever",
		"display_orientation": "True",
		"display_gender": "True",
		"display_pronouns": "True",
    "socials": 
    {
        "facebook": "linktofacebook",
        "instagram": "linktoinstagram",
        "twitter": "linktotwitter",
        "discord_id": "discord_id"
    },
		"interests": [ "interest1", "interest2", "interest3"],
		"games": [ "d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f"]
}
```

RESPONSE:

```jsx
"User created" 201 CREATED
```

### Get user

REQUEST:

```jsx
GET url/user?user_id=<user_id>
```

HEADERS:

Authorization : <ACCESS_TOKEN>

RESPONSE:

```jsx
{
		"id": "d69-4170-45d2-ad81-3e36794f",
    "username": "name",
    "email": "name@gmail.com",
    "gender": "female",
    "age": 20,
    "orientation": "heterosexual",
		"pronouns": "she/her",
    "about_me": "Lorem ipsum or whatever",
    "socials": 
    {
        "facebook": "linktofacebook",
        "instagram": "linktoinstagram",
        "twitter": "linktotwitter",
        "discord_id": "discord_id"
    },
		"interests": [ "interest1", "interest2", "interest3"],
		"games": [ "d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f"],
		"teammates": [ "d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f"],
		"new_follows": [ "d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f"]
			
}

```

new_follows is a list of id's of users that recently followed the user it works as a notification

### Update user

REQUEST:

```jsx
PUT url/user?user_id=<user_id>
```

HEADERS:

Authorization : <ACCESS_TOKEN>

BODY (json):

```jsx
{
    "username": "name",
    "password": "password123",
    "email": "name@gmail.com",
    "gender": "female",
    "age": 20,
    "orientation": "heterosexual",
		"pronouns": "she/her",
    "about_me": "Lorem ipsum or whatever",
		"display_orientation": "True",
		"display_gender": "True",
		"display_pronouns": "True",
    "socials": 
    {
        "facebook": "linktofacebook",
        "instagram": "linktoinstagram",
        "twitter": "linktotwitter",
        "discord_id": "discord_id"
    },
}
```

RESPONSE:

```jsx
"USER UPDATED" 200 OK
```

### Delete user

REQUEST:

```jsx
DELETE url/user?user_id=<user_id>
```

HEADERS:

Authorization : <ACCESS_TOKEN>

RESPONSE:

```jsx
"USER REMOVED" 200 OK
```

### Add user interest

This endpoint add new interests to user's interests list

REQUEST:

```jsx
POST url/interest?user_id=<user_id>
```

HEADERS:

Authorization : <ACCESS_TOKEN>

BODY (JSON):

```jsx
{
	"interest": "interest1"
}
```

RESPONSE:

```jsx
"INTEREST ADDED" 201 CREATED
```

### Remove user interest

REQUEST:

```jsx
DELETE url/interest?user_id=<user_id>
```

HEADERS:

Authorization : <ACCESS_TOKEN>

BODY (JSON):

```jsx
{
	"interest": "interest1"
}
```

RESPONSE:

```jsx
"INTEREST REMOVED" 200 OK
```

### Add game

This endpoint adds game to users games list

REQUEST:

```jsx
POST url/usergame?user_id=<user_id>
```

HEADERS:

Authorization : <ACCESS_TOKEN>

BODY (JSON):

```jsx
{
	"game": "game's name or id whatever you have on the frontend"
}
```

RESPONSE:

```jsx
"GAME ADDED" 201 CREATED
```

### Remove game

REQUEST:

```jsx
DELETE url/usergame?user_id=<user_id>
```

HEADERS:

Authorization : <ACCESS_TOKEN>

BODY (JSON):

```jsx
{
		"game": "game's name or id whatever you have on the frontend"
}
```

RESPONSE:

```jsx
"GAME REMOVED" 200 OK
```

### Add profile picture

REQUEST:

```jsx
POST url/user/profile_pic?user_id=<user_id>
```

HEADERS:

Authorization : <ACCESS_TOKEN>

BODY (FILE):

profile_picture.jpg or profile_picture.png

RESPONSE:

```jsx
"PROFILE PICTURE ADDED" 201 CREATED
```

### Update profile picture

REQUEST:

```jsx
PUT url/user/profile_pic?user_id=<user_id>
```

HEADERS:

Authorization : <ACCESS_TOKEN>

BODY (FILE):

profile_picture.jpg or profile_picture.png

RESPONSE:

```jsx
"PROFILE PICTURE UPDATED" 200 OK
```

### Remove profile picture

REQUEST:

```jsx
DELETE url/user/profile_pic?user_id=<user_id>
```

HEADERS:

Authorization : <ACCESS_TOKEN>

BODY:

EMPTY

RESPONSE:

```jsx
"PROFILE PICTURE REMOVED" 200 OK
```

## Recommendations

### Follow (add) other user

REQUEST:

```jsx
POST url/recommendations/follow?user_id=<user_id>
```

 

HEADERS:

Authorization: <ACCESS_TOKEN>

BODY:

```jsx
{
	"added_user_id": "d69-4170-45d2-ad81-3e36794f"
}
```

RESPONSE:

```jsx
"USER FOLLOWED" 200 OK

or

"USERS ARE NOW TEAMMATES" 200 OK
```

RESPONSE HEADERS:

for "USER FOLLOWED" response "X-Teammates" header is set to false

for "USERS ARE NOW TEAMMATES response "X-Teammates" header is set to true

based on that you can show the notification when both users added each other

### Add ignored user

Use this endpoints to inform the backend that recommended user was ignored

REQUEST:

```jsx
POST url/recommendations/ignored?user_id=<user_id>
```

```jsx
{
		"users": [ 	"d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f"]
}
```

RESPONSE:

 

```jsx
"USERS INGORED", 200 OK
```

### Get recommended users based on games

REQUEST:

```jsx
GET url/recommendations/gaming?user_id=<user_id>
```

BODY:

EMPTY

RESPONSE:

```jsx
{
	["d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f"]
}

200 OK
```

### Get recommended users based on interests

REQUEST:

```jsx
GET url/recommendations/gaming?user_id<user_id>
```

BODY:

EMPTY

RESPONSE:

```jsx
{
	["d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f", "d69-4170-45d2-ad81-3e36794f"]
}

200 OK
```

## Forum

### Get forum threads from specified forum section

REQUEST:

```jsx
GET url/forum/threads?forum_section=<forum_section_name>
```

BODY:

EMPTY

RESPONSE:

```jsx
{
		"id": "d69-4170-45d2-ad81-3e36794f",
		"author": "d69-4170-45d2-ad81-3e36794f",
		"title": "Random title",
		"creation_time": "2012-04-23T18:25:43.511Z",
		"text": "Random content of the thread",
}

200 OK
```

### Add forum thread

REQUEST:

```jsx
POST url/forum/threads?forum_section=<forum_section_name>
```

BODY:

```jsx
{
		"author": "d69-4170-45d2-ad81-3e36794f",
		"title": "Random title",
		"creation_time": "2012-04-23T18:25:43.511Z",
		"text": "Random content of the thread",
}
```

RESPONSE

```jsx
"FORUM THREAD CREATED" 201 CREATED
```

### Remove forum thread

REQUEST:

```jsx
DELETE url/forum/threads?thread_id=<thread_id>
```

BODY:

EMPTY

RESPONSE:

```jsx
"FORUM THREAD REMOVED" 200 OK
```

### Get comments under the thread

REQUEST:

```jsx
GET url/forum/comments?thread_id=<thread_id>
```

BODY:

EMPTY

RESPONSE:

```jsx
{
		[
				{ "id": "d69-4170-45d2-ad81-3e36794f", "text": "randomtext",
					 "creation_time": "2012-04-23T18:25:43.511Z", "author": "d69-4170-45d2-ad81-3e36794f",
						"thread": "d69-4170-45d2-ad81-3e36794f", "reply_to": "d69-4170-45d2-ad81-3e36794f"
				},

				{ "id": "d69-4170-45d2-ad81-3e36794f", "text": "randomtext",
					 "creation_time": "2012-04-23T18:25:43.511Z", "author": "d69-4170-45d2-ad81-3e36794f",
						"thread": "d69-4170-45d2-ad81-3e36794f", "reply_to": "d69-4170-45d2-ad81-3e36794f"
				},

				{ "id": "d69-4170-45d2-ad81-3e36794f", "text": "randomtext",
					 "creation_time": "2012-04-23T18:25:43.511Z", "author": "d69-4170-45d2-ad81-3e36794f",
						"thread": "d69-4170-45d2-ad81-3e36794f", "reply_to": "d69-4170-45d2-ad81-3e36794f"
				}

		]

}
```

### Add comment

REQUEST:

```jsx
POST url/forum/comments?thread_id=<thread_id>
```

BODY:

```jsx
{  
		"text": "randomtext",
		"creation_time": "2012-04-23T18:25:43.511Z", 
		"author": "d69-4170-45d2-ad81-3e36794f",
		"thread": "d69-4170-45d2-ad81-3e36794f", 
		"reply_to": "d69-4170-45d2-ad81-3e36794f"
}
```

RESPONSE:

```jsx
"COMMENT ADDED" 201 CREATED
```

### Remove comment

REQUEST:

```jsx
DELETE url/forum/comments?comment_id=<comment_id>
```

BODY:

EMPTY

RESPONSE:

```jsx
"COMMENT REMOVED" 200 OK
```