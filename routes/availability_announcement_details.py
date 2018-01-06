from flask import Blueprint, render_template, abort
from flask import Flask, jsonify, request
from handler.availabilityAnnouncementDetails import AvailabilityAnnouncementDetailsHandler

availability_announcement_details_route = Blueprint('availability_announcement_details_route', __name__)

@availability_announcement_details_route.route('/api/announcementdetails', methods=['GET', 'POST'])
def getAllAnnouncementDetails():
    if not request.args:
        return AvailabilityAnnouncementDetailsHandler().getAllAnnouncementDetails()
    else:
        return AvailabilityAnnouncementDetailsHandler().searchAnnouncementDetails()

@availability_announcement_details_route.route('/api/announcementdetails/<int:ann_id>,<int:rid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getAnnouncementDetailsById(ann_id, rid):
    if request.method == 'GET':
        return AvailabilityAnnouncementDetailsHandler().getAnnouncementDetailsById(ann_id, rid)


