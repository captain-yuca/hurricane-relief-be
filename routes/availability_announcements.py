from flask import Blueprint, render_template, abort, request
from handler.availability_announcements import AvailabilityAnnouncementsHandler

availability_announcements_route = Blueprint('availability_announcements_route', __name__)

@availability_announcements_route.route('/api/announcements', methods=['GET'])
def getAllAnnouncements():
    if request.method == 'GET':
        if not request.args:
            return AvailabilityAnnouncementsHandler().getAllAnnouncements()
        else:
            return AvailabilityAnnouncementsHandler().searchAnnouncements(request.args)
    else:
        return jsonify(Error="Method not allowed. "), 405

@availability_announcements_route.route('/api/announcements/<int:annid>', methods=['GET'])
def getAnnouncementById(annid):
    if request.method == 'GET':
        return AvailabilityAnnouncementsHandler().getAnnouncementById(annid)
    else:
        return jsonify(Error="Method not allowed. "), 405
