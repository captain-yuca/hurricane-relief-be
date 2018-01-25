from flask import jsonify
from dao.availability_announcements import AvailabilityAnnouncementsDAO
from models.availability_announcement import AvailabilityAnnouncement

class AvailabilityAnnouncementsHandler:

    def getAllAnnouncements(self):
        dao = AvailabilityAnnouncementsDAO()
        announcement_list = dao.getAllAnnouncements()
        result =  AvailabilityAnnouncement().build_dict_from_table(announcement_list)
        return jsonify(result)

    def getAnnouncementById(self, ann_id):
        dao = AvailabilityAnnouncementsDAO()
        table = dao.getAnnouncementByIdWithDetails(ann_id)
        if not table:
            return jsonify(Error = "Availability Announcement Not Found"), 404
        else:
            result = AvailabilityAnnouncement().build_dict_from_table_details(table)
            return jsonify(announcement = result)

    def searchAnnouncements(self, args):
        allowedKeys= {"rid", "rname"}
        for key in args.keys():
            if key not in allowedKeys:
                return jsonify(Error="Malformed query string"), 400

        dao = AvailabilityAnnouncementsDAO()
        announcements_list = dao.getAnnouncementsByParameters(args)
        result_list=[]
        for row in announcements_list:
            announcement = AvailabilityAnnouncement().build_dict_from_row_resource(row)
            result_list.append(announcement)
        return jsonify(announcements=result_list)
