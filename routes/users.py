from flask import Blueprint, render_template, abort, request, jsonify
from handler.users import UsersHandler

users_route = Blueprint('users_route', __name__)

@users_route.route('/api/users', methods=['GET','POST'])
def getAllUsers():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        if not request.args:
            return UsersHandler().getAllUsers()
        else:
            return UsersHandler().searchUsers(request.args)
    else:
        return jsonify(Error="Method not allowed. "), 405

@users_route.route('/api/users/<int:uid>', methods=['GET','PUT','DELETE'])
def getUserById(uid):
    if request.method == 'GET':
        return UsersHandler().getUserById(uid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405

@users_route.route('/api/users/<int:uid>/addresses', methods=['GET','POST'])
def getAddressesByUserId(uid):
    if request.method == 'GET':
        return UsersHandler().getAddressesByUserId(uid)
    elif request.method == 'POST':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405
