from flask import jsonify
from dao.resourceRequestDetails import ResourceRequestDetailsDAO
from models.resourceRequestDetails import ResourceRequestDetails

class ResourceRequestDetailsHandler:

    def getAllRequestDetails(self):
        dao = ResourceRequestDetailsDAO()
        requestDetails_list = dao.getAllRequestDetails()
        result_list = []
        for row in requestDetails_list:
            result = ResourceRequestDetails().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Request_Details=result_list)

    def getRequestDetailsById(self, req_id, rid):
        dao = ResourceRequestDetailsDAO()
        row = dao.getRequestDetailsById(req_id, rid)
        if not row:
            return jsonify(Error="Resource Request Detail Not Found"), 404
        else:
            requestDetails = ResourceRequestDetails().build_dict_from_row(row)
            return jsonify(Request_Details=requestDetails)

    def searchRequestDetails(self, args):
        req_id = args.get("req_id")
        rid = args.get("rid")
        qty = args.get("qty")
        dao = ResourceRequestDetailsDAO()
        requestDetails_list = []
        if(len(args) == 2) and req_id and qty:
            requestDetails_list = dao.getRequestDetailsByReqidAndQty(req_id, qty)
        elif(len(args) == 2) and rid and qty:
            requestDetails_list = dao.getRequestDetailsByRisAndQty(rid, qty)
        elif(len(args) == 1) and req_id:
            requestDetails_list = dao.getRequestDetailsByReqid(req_id)
        elif(len(args) == 1) and rid:
            requestDetails_list = dao.getRequestDetailsByRid(rid)
        elif(len(args) == 1) and qty:
            requestDetails_list = dao.getRequestDetailsByQty(qty)
        else:
            return jsonify(Error="Malformed Query String"), 400
        result_list = []
        for row in requestDetails_list:
            result = ResourceRequestDetails.build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Request_Details=result_list)