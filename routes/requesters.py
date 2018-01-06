from flask import Blueprint, render_template, abort
from handler.requesters import RequestersHandler

requesters_route = Blueprint('requesters_route', __name__)

@requesters_route.route('/api/requesters', methods=['GET','POST'])
def getAllRequesters():
    return RequestersHandler().getAllRequesters()

@requesters_route.route('/api/requesters/<int:nid>', methods=['GET','POST','DELETE','UPDATE'])
def getRequesterById(nid):
    if request.method == 'GET':
        return RequestersHandler().getRequesterById(nid)
