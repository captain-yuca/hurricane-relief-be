from flask import Blueprint, render_template, abort, request
from handler.availability_announcements import AvailabilityAnnouncementsHandler

availability_announcements_route = Blueprint('availability_announcements_route', __name__)

@availability_announcements_route.route('/api/announcements', methods=['GET', 'POST'])
def getAllAnnouncements():
    if not request.args:
        return AvailabilityAnnouncementsHandler().getAllAnnouncements()
    else:
        pass
@availability_announcements_route.route('/api/announcements/<int:annid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getAnnouncementById(annid):
    if request.method == 'GET':
        return AvailabilityAnnouncementsHandler().getAnnouncementById(annid)
