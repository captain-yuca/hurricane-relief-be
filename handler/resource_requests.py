from flask import jsonify
from dao.resource_requests import ResourceRequestsDAO
from models.resource_request import ResourceRequest

class ResourceRequestsHandler:

    def getAllRequests(self):
        dao = ResourceRequestsDAO()
        request_list = dao.getAllRequests()
        result_list=[]
        for row in request_list:
            request = ResourceRequest().build_dict_from_row_resource(row)
            result_list.append(request)
        return jsonify(ResourceRequests=result_list)

    def getRequestById(self, req_id):
        dao = ResourceRequestsDAO()
        request = dao.getRequestByIdWithDetails(req_id)
        if not request:
            return jsonify(Error = "Availability Announcement Not Found"), 404
        else:
            result = ResourceRequest().build_dict_from_table_details(request)
            return jsonify(ResourceRequest = result)

    #added by Herbert
    def getRequestedResources(self):
        dao = ResourceRequestsDAO()
        request_list = dao.getRequestedResources()
        result_list=[]
        for row in request_list:
            request = ResourceRequest().build_dict_from_row2(row)
            result_list.append(request)
        return jsonify(ResourceRequests=result_list)
