from flask import jsonify
from dao.resource_requests import ResourceRequestsDAO
from models.resource_request import ResourceRequest

class ResourceRequestsHandler:

    def getAllRequests(self):
        dao = ResourceRequestsDAO()
        request_list = dao.getAllRequests()
        result_list=ResourceRequest().build_dict_from_table_resources(request_list)
        return jsonify(ResourceRequests=result_list)

    def getAnnouncementById(self, req_id):
        dao = ResourceRequestsDAO()
        row = dao.getRequesttById(req_id)
        if not row:
            return jsonify(Error = "Availability Announcement Not Found"), 404
        else:
            request = ResourceRequest().build_dict_from_row(row)
            return jsonify(ResourceRequest = request)
