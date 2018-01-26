from flask import jsonify

from dao.categories import CategoriesDAO
from dao.resourceRequestDetails import ResourceRequestDetailsDAO
from dao.resource_requests import ResourceRequestsDAO
from dao.resources import ResourcesDAO
from dao.users import UsersDAO
from dao.requesters import RequestersDAO

from models.requester import Requester
from models.address import Address
from models.resource_request import ResourceRequest


class RequestersHandler:

    def getAllRequesters(self):
        dao = RequestersDAO()
        requesters_list = dao.getAllRequesters()
        result_list=[]
        for row in requesters_list:
            requester = Requester().build_dict_from_row(row)
            result_list.append(requester)
        return jsonify(result_list)

    def getRequesterById(self, nid):
        dao = RequestersDAO()
        row = dao.getRequesterById(nid)
        if not row:
            return jsonify(Error = "Requester Not Found"), 404
        else:
            requester = Requester().build_dict_from_row(row)
            return jsonify(requester)

    def getRequestersCountByRegion(self):
        dao = RequestersDAO()
        counts_list = dao.getRequestersCountByRegion()
        result_list = []
        for row in counts_list:
            count = Address().build_dict_from_row_count(row)
            result_list.append(count)
        return jsonify(result_list)

    def insertRequester(self, form):
        daou = UsersDAO()
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            uid = form['uid']
            if uid and daou.getUserById(uid):
                dao = RequestersDAO()
                nid = dao.insert(uid)
                result = Requester().build_dict_from_row(dao.getRequesterById(nid))
                return jsonify(result), 201
            else:
                return jsonify(Error="Unexpected attributes in post requester"), 400

    def insertRequest(self, form, nid):
        # New Resource
        if len(form) == 3:
            rname = form['rname']
            catid = form['catid']
            qty = form['qty']
            if rname and catid and qty:
                dao = ResourcesDAO()
                resource = dao.getResourcesByRname(rname)
                if not resource:
                    dao2 = CategoriesDAO()
                    if not dao2.getCategoryById(catid):
                        return jsonify(Error="Category Not Found"), 404
                    rid = dao.insert(rname, catid)
                else:
                    rid = (resource[0])[0]


                dao = ResourceRequestsDAO()
                req_id = dao.insertRequest(nid)

                dao3 = ResourceRequestDetailsDAO()
                dao3.insertRequestDetails(req_id, rid, qty)

                table = dao.getRequestByIdWithDetails(req_id)

                if not table:
                    return jsonify(Error="Request Not Found"), 404
                else:
                    print(table)
                    result = ResourceRequest().build_dict_from_table_details(table)
                    return jsonify(result)
        elif len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            # Existing Resource
            rid = form['rid']
            qty = form['qty']

            if rid and qty:
                dao = ResourcesDAO()
                if not dao.getResourceById(rid):
                    return jsonify(Error="Resource Not Found"), 404

                dao2 = ResourceRequestsDAO()
                reqid = dao2.insertRequest(nid)
                dao3 = ResourceRequestDetailsDAO()
                dao3.insertRequestDetails(reqid, rid, qty)

                result = ResourceRequest().build_dict_from_row_resource(dao2.getRequestByIdWithDetails2(reqid))
                return jsonify(result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
    def getRequestByIds(self, nid, req_id): #new by herbert
        dao = RequestersDAO()
        row = dao.getRequesterById()
        if not row:
            return jsonify(Error="Requester Not Found"), 404
        else:
            dao2 = ResourceRequestsDAO()
            requests_list = dao2.getRequestsByNid(nid)
            if not requests_list[0]:
                return jsonify(Error="Request Not Found"), 404
            dao = ResourceRequestsDAO
            result =[]
            result.append(dao.getRequestByIdWithDetails(req_id))
            newresult = ResourceRequest().build_dict_from_table_no_nid(result)
            return jsonify(newresult)
    def getRequestsByNid(self, nid):
        dao = RequestersDAO()
        row = dao.getRequesterById(nid)
        if not row:
            return jsonify(Error="Requester Not Found"), 404
        else:
            dao2 = ResourceRequestsDAO()
            requests_list = dao2.getRequestsByNid(nid)
            if not requests_list:
                return jsonify([])
            result_list = ResourceRequest().build_dict_from_table_no_nid(requests_list)
            return jsonify(result_list)

    def insertRequestDetailsByReqId(self, form, req_id):

        # Existing Resource
        if 2 == len(form):
            rid = form['rid']
            qty = form['qty']

            if rid and qty:
                dao = ResourcesDAO()
                if not dao.getResourceById(rid):
                    return jsonify(Error="Resource Not Found"), 404

                dao2 = ResourceRequestsDAO()
                request = dao2.getRequestByIdWithDetails(req_id)
                if not request:
                    return jsonify(Error="Request Not Found"), 404
                else:
                    nid = request[0]

                dao3 = ResourceRequestDetailsDAO()
                if not dao3.getRequestDetailsById(req_id, rid):
                    dao3.insertRequestDetails(req_id, rid, qty)
                else:
                    return jsonify(Error="Duplicate Primary Key"), 400

                table = dao2.getRequestByIdWithDetails2(req_id)
                if not table:
                    return jsonify(Error="Resource Request Not Found"), 404
                else:
                    result = ResourceRequest().build_dict_from_row_resource(table)
                    return jsonify(result)
        elif len(form) != 3:
                return jsonify(Error="Malformed Post Request"), 400

        # New Resource
        else:
            rname = form['rname']
            catid = form['catid']
            qty = form['qty']
            if rname and catid and qty:
                dao = ResourcesDAO()
                dao2 = CategoriesDAO()

                # Check if resource exists
                resource = dao.getResourcesByRname(rname)
                if not resource:
                    # Create new resource
                    if not dao2.getCategoryById(catid):
                        return jsonify(Error="Category Not Found"), 404
                    rid = dao.insert(rname, catid)
                else:
                    rid = (resource[0])[0]


                dao3 = ResourceRequestsDAO()
                request = dao3.getRequestByIdWithDetails(req_id)
                if not request or not request[0]:
                    return jsonify(Error="Request Not Found"), 404
                else:
                    nid = request[0][2]
                dao4 = ResourceRequestDetailsDAO()
                if not dao4.getRequestDetailsById(req_id, rid):
                    dao4.insertRequestDetails(req_id, rid, qty)
                else:
                    return jsonify(Error="Duplicate Primary Key"), 400

                table = dao3.getRequestByIdWithDetails(req_id)
                if not table:
                    return jsonify(Error="Request Not Found"), 404
                else:
                    result = ResourceRequest().build_dict_from_table_details(table)
                    return jsonify(result)
            else:
                return jsonify(Error="Malformed Post Request"), 400

    def updateRequestDetailsByReqId(self, form, req_id):
        if len(form) == 2:
            rid = form['rid']
            qty = form['qty']

            if rid and qty:

                rdao = ResourcesDAO()
                if not rdao.getResourceById(rid):
                    return jsonify(Error="Resource Not Found")
