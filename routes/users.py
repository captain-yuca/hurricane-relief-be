from flask import Blueprint, render_template, abort, request, jsonify
from handler.users import UsersHandler

users_route = Blueprint('users_route', __name__)

@users_route.route('/api/users', methods=['GET','POST'])
def getAllUsers():
    """ Returns all users. """
    if request.method == 'POST':
        return UsersHandler().insertUser(request.form)
    elif request.method == 'GET':
        if not request.args:
            return UsersHandler().getAllUsers()
        else:
            return UsersHandler().searchUsers(request.args)
    else:
        return jsonify(Error="Method not allowed. "), 405

@users_route.route('/api/users/<int:uid>', methods=['GET','PUT','DELETE', 'PUT'])
def getUserById(uid):
    """ Returns the user with the specified uid. """
    if request.method == 'GET':
        return UsersHandler().getUserById(uid)
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405

@users_route.route('/api/users/<int:uid>/purchases', methods=['GET','POST'])
def getPurchasesByUserId(uid):
    """ Returns all purchases made by the speicied user with uid. """
    if request.method == 'GET':
        return UsersHandler().getPurchasesByUserId(uid)
    elif request.method == 'POST':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405

@users_route.route('/api/users/<int:uid>/purchases/<int:pi_id>', methods=['GET','POST'])
def getUserPurchaseById(uid,pi_id):
    """ Returns a purchase with the specified pi_id made by the user with uid. """
    if request.method == 'GET':
        return UsersHandler().getUserPurchaseById(uid, pi_id)
    elif request.method == 'POST':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405

@users_route.route('/api/users/<int:uid>/purchases/<int:pi_id>/details', methods=['GET','POST'])
def getPurchaseDetailsById(uid,pi_id):
    """ Returns all details of a purchase with the specified pi_id made by the user with uid. """

    if request.method == 'GET':
        return UsersHandler().getPurchaseDetailsById(uid, pi_id)
    elif request.method == 'POST':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405

@users_route.route('/api/users/<int:uid>/addresses', methods=['GET','POST'])
def getAddressesByUserId(uid):
    """ Returns all addresses tied to the user with uid. """
    if request.method == 'GET':
        return UsersHandler().getAddressesByUserId(uid)
    elif request.method == 'POST':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405
