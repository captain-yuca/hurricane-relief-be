from flask import jsonify
from dao.resource_requests import ResourceRequestsDAO
from models.resource_request import ResourceRequest

class ResourceRequestsHandler:

    def getAllRequests(self):
        dao = ResourceRequestsDAO()
        request_list = dao.getAllRequests()
        result_list = ResourceRequest().build_dict_from_table(request_list)
        return jsonify(result_list)

    def getRequestById(self, req_id):
        dao = ResourceRequestsDAO()
        request = dao.getRequestByIdWithDetails(req_id)
        if not request:
            return jsonify(Error = "Availability Announcement Not Found"), 404
        else:
            result = ResourceRequest().build_dict_from_table_details(request)
            return jsonify(result)

    #added by Herbert
    def getRequestedResources(self):
        dao = ResourceRequestsDAO()
        request_list = dao.getRequestedResources()
        result_list=[]
        for row in request_list:
            request = ResourceRequest().build_dict_from_row2(row)
            result_list.append(request)
        return jsonify(result_list)

    def searchRequests(self, args):
        allowedKeys= {"rid", "rname", "catname", "catid"}
        for key in args.keys():
            if key not in allowedKeys:
                return jsonify(Error="Malformed query string"), 400

        dao = ResourceRequestsDAO()
        request_list = dao.getRequestsByParameters(args)
        result_list = ResourceRequest().build_dict_from_table(request_list)
        return jsonify(result_list)
