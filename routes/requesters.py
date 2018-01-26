from flask import Blueprint, render_template, abort, request, jsonify
from handler.requesters import RequestersHandler

requesters_route = Blueprint('requesters_route', __name__)

@requesters_route.route('/api/requesters', methods=['GET','POST'])
def getAllRequesters():
    if request.method == 'GET':
        return RequestersHandler().getAllRequesters()
    elif request.method == 'POST':
        return RequestersHandler().insertRequester(request.get_json())
    else:
        return jsonify(Error="Method Not Allowed"), 405

@requesters_route.route('/api/requesters/<int:nid>', methods=['GET'])
def getRequesterById(nid):
    if request.method == 'GET':
        return RequestersHandler().getRequesterById(nid)
    else:
        return jsonify(Error="Method Not Allowed"), 405

@requesters_route.route('/api/requesters/countPerRegion', methods=['GET', 'POST'])
def getRequestersCountPerRegion():
    if request.method == 'GET':
        return RequestersHandler().getRequestersCountByRegion()
    else:
        pass

@requesters_route.route('/api/requesters/<int:nid>/requests', methods=['GET', 'POST'])
def getRequestsByNid(nid):
    if request.method == 'GET':
        if not request.args:
            return RequestersHandler().getRequestsByNid(nid)
        else:
            pass
    elif request.method == 'POST':
        return RequestersHandler().insertRequest(request.get_json(), nid)
    else:
        return jsonify(Error="Method not allowed"), 405

@requesters_route.route('/api/requesters/<int:nid>/requests/<int:req_id>', methods=['GET', 'POST', 'PUT'])
def getRequestDetailsByReqId(nid, req_id):
    if request.method == 'GET':
        if not request.args:
            return RequestersHandler().getRequestsByNid(nid)
        else:
            pass
    elif request.method == 'POST':
        return RequestersHandler().insertRequestDetailsByReqId(request.get_json(), req_id)
    elif request.method == 'PUT':
        return RequestersHandler().updateRequestDetailsByReqId(request.get_json(), req_id)
