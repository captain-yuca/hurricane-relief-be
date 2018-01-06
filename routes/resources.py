from flask import Blueprint, render_template, abort, request
from handler.resources import ResourcesHandler

resources_route = Blueprint('resources_route', __name__)


@resources_route.route('/api/resources', methods=['GET', 'POST'])
def getAllResources():
    if not request.args:
        return ResourcesHandler().getAllResources()
    else:
        return ResourcesHandler().searchResources(request.args)

@resources_route.route('/api/resources/<int:rid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getResourceById(rid):
    if request.method == 'GET':
        return ResourcesHandler().getResourceById(rid)
