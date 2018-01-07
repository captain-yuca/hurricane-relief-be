from flask import Blueprint, render_template, abort, jsonify, request
from handler.resources import ResourcesHandler

resources_route = Blueprint('resources_route', __name__)


@resources_route.route('/api/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().searchResources(request.args)
    else:
        return jsonify(Error="Method Not Allowed"), 405

@resources_route.route('/api/resources/<int:rid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getResourceById(rid):
    if request.method == 'GET':
        return ResourcesHandler().getResourceById(rid)
