from flask import Blueprint, render_template, abort, jsonify, request
from handler.resources import ResourcesHandler

resources_route = Blueprint('resources_route', __name__)


@resources_route.route('/api/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        return ResourcesHandler().insertResource(request.get_json())
    elif request.method == 'GET':
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().searchResources(request.args)
    else:
        return jsonify(Error="Method Not Allowed"), 405

@resources_route.route('/api/resources/<int:rid>', methods=['GET', 'PUT'])
def getResourceById(rid):
    if request.method == 'GET':
        return ResourcesHandler().getResourceById(rid)
    elif request.method == 'PUT':
        return ResourcesHandler().updateResource(rid, request.get_json())
    else:
        return jsonify(Error="Method Not Allowed"), 405
