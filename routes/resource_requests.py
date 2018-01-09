from flask import Blueprint, render_template, abort, request
from handler.resource_requests import ResourceRequestsHandler

resource_requests_route = Blueprint('resource_requests_route', __name__)

@resource_requests_route.route('/api/requests', methods=['GET', 'POST'])
def getAllRequests():
    if not request.args:
        return ResourceRequestsHandler().getAllRequests()
    else:
        pass
@resource_requests_route.route('/api/requests/<int:reqid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getRequestById(reqid):
    if request.method == 'GET':
        return ResourceRequestsHandler().getRequestById(reqid)
#added by herbert, im bad with routes. verify
@resource_requests_route.route('/api/requests/requestedresources', methods=['GET', 'POST'])
def getRequestedRequests():
    if request.method == 'GET':
        return ResourceRequestsHandler().getRequestedResources()
    else:
        pass
