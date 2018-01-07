from flask import Blueprint, render_template, abort
from flask import Flask, jsonify, request
from handler.resourceRequestDetails import ResourceRequestDetailsHandler

resource_request_details_route = Blueprint('resource_request_details_route', __name__)

@resource_request_details_route.route('/api/requestdetails', methods=['GET', 'POST'])
def getAllRequestDetails():
    if not request.args:
        return ResourceRequestDetailsHandler().getAllRequestDetails()
    else:
        return ResourceRequestDetailsHandler().searchRequestDetails(request.args)

@resource_request_details_route.route('/api/requestdetails/<int:req_id>,<int:rid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getRequestDetailsById(req_id, rid):
    if request.method == 'GET':
        return ResourceRequestDetailsHandler().getRequestDetailsById(req_id, rid)
