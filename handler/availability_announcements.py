from flask import jsonify
from dao.availability_announcements import AvailabilityAnnouncementsDAO
from models.availability_announcement import AvailabilityAnnouncement

class AvailabilityAnnouncementsHandler:

    def getAllAnnouncements(self):
        dao = AvailabilityAnnouncementsDAO()
        announcement_list = dao.getAllAnnouncements()
        result_list=[]
        for row in announcement_list:
            availabilityAnnouncement = AvailabilityAnnouncement().build_dict_from_row(row)
            result_list.append(availabilityAnnouncement)
        return jsonify(AvailabilityAnnouncements=result_list)

    def getAnnouncementById(self, ann_id):
        dao = AvailabilityAnnouncementsDAO()
        row = dao.getAnnouncementById(ann_id)
        if not row:
            return jsonify(Error = "Availability Announcement Not Found"), 404
        else:
            availabilityAnnouncement = AvailabilityAnnouncement().build_dict_from_row(row)
            return jsonify(AvailabilityAnnouncement = availabilityAnnouncement)
