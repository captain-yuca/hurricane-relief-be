from flask import jsonify
from dao.availabilityAnnoucementDetails import AvailabilityAnnoucementDetailsDAO
from models.availabilityAnnouncementDetails import AvailabilityAnnouncementDetails

class AvailabilityAnnouncementDetailsHandler:

    def getAllAnnouncementDetails(self):
        dao = AvailabilityAnnoucementDetailsDAO()
        announcementDetails_list = dao.getAllAnnouncementDetails()
        result_list = []
        for row in announcementDetails_list:
            result = AvailabilityAnnouncementDetails().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(result_list)

    def getAnnouncementDetailsById(self, ann_id, rid):
        dao = AvailabilityAnnoucementDetailsDAO()
        row = dao.getAnnouncementDetailsById(ann_id, rid)
        if not row:
            return jsonify(Error="Availability Announcement Detail Not Found"), 404
        else:
            announcementDetails = AvailabilityAnnouncementDetails().build_dict_from_row(row)
            return jsonify(announcementDetails)

    def searchAnnouncementDetails(self, args):
        ann_id = args.get("ann_id")
        rid = args.get("rid")
        qty = args.get("qty")
        priceattime = args.get("priceattime")
        dao = AvailabilityAnnoucementDetailsDAO()
        announcementDetails_list = []
        if(len(args) == 3) and ann_id and qty and priceattime:
            announcementDetails_list = dao.getAnnouncementDetailsByAnnidQtyAndPriceattime(ann_id, qty, priceattime)
        elif(len(args) == 3) and rid and qty and priceattime:
            announcementDetails_list = dao.getAnnouncementDetailsByRidQtyAndPriceattime(rid, qty, priceattime)
        elif(len(args) == 2) and ann_id and qty:
            announcementDetails_list = dao.getAnnouncementDetailsByAnnidAndQty(ann_id, qty)
        elif(len(args ) == 2) and ann_id and priceattime:
            announcementDetails_list = dao.getAnnouncementDetailsByAnnidAndPriceattime(ann_id, priceattime)
        elif(len(args) == 2) and rid and qty:
            announcementDetails_list = dao.getAnnouncementDetailsByRidAndQty(rid, qty)
        elif(len(args) == 2) and rid and priceattime:
            announcementDetails_list = dao.getAnnouncementDetailsByRidAndPriceattime(rid, priceattime)
        elif(len(args) == 2) and qty and priceattime:
            announcementDetails_list = dao.getAnnouncementDetailsByQtyAndPriceattime(qty, priceattime)
        elif(len(args) == 1) and ann_id:
            announcementDetails_list = dao.getAnnouncementDetailsByAnnid(ann_id)
        elif(len(args) == 1) and rid:
            announcementDetails_list = dao.getAnnouncementDetailsByRid(rid)
        elif(len(args) == 1) and qty:
            announcementDetails_list = dao.getAnnouncementDetailsByQty(qty)
        elif(len(args) == 1) and priceattime:
            announcementDetails_list = dao.getAnnouncementDetailsByPriceattime(priceattime)
        else:
            return jsonify(Error="Malformed Query String"), 400
        result_list = []
        for row in announcementDetails_list:
            result = AvailabilityAnnouncementDetails().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(result_list)
