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


@hug.post('/api/v1/addbm')
def add_bookmark(username, bmname, bmurl, bmdesc):
    result = db.add_bookmark(username, bmname, bmurl, bmdesc)
    if result:
        return {'result': True}
    else:
        return {'result': False, 'message': "could not add bookmark"}


@hug.get('/api/v1/lsbm')
def list_bookmarks(username):
    result = db.get_bookmarks(username)
    if result:
        return {'result': True, 'data': result}
    else:
        return {'result': False, 'message': "something bad happened"}


@hug.response_middleware()
def add_access_control(request, response, resource):
    response.set_header('Access-Control-Allow-Origin', 'http://192.168.1.61')
