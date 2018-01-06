from flask import Blueprint, render_template, abort
from handler.users import UsersHandler

users_route = Blueprint('users_route', __name__)

@users_route.route('/api/users', methods=['GET','POST'])
def getAllUsers():
    return UsersHandler().getAllUsers()

@users_route.route('/api/users/<int:uid>', methods=['GET','POST','DELETE','UPDATE'])
def getUserById(uid):
    if request.method == 'GET':
        return UsersHandler().getUserById(uid)

@users_route.route('/api/users/<int:uid>/addresses', methods=['GET','POST','DELETE','UPDATE'])
def getAddressesByUserId(uid):
    if request.method == 'GET':
        return UsersHandler().getAddressesByUserId(uid)
