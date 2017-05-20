"""contains api endpoints for bookmark.io"""

import hug
import db


@hug.post('/api/v1/login')
def login(username):
    result = db.get_user(username)
    if result:
        return {'result': True, 'username': result}
    else:
        return {'result': False, 'message': "user does not exist"}


@hug.post('/api/v1/register')
def register(username):
    result = db.add_user(username)
    if result:
        return {'result': True, 'username': username}
    else:
        return {'result': False, 'message': "user already exists"}


@hug.response_middleware()
def add_access_control(request, response, resource):
    response.set_header('Access-Control-Allow-Origin', 'http://192.168.1.61')
