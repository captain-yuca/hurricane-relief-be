from flask import jsonify

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

    # def getAddressesByUserId(self, sid):
    #     userDao = UsersDAO()
    #     addressesDao = AddressesDAO()
    #     user = userDao.getUserById(sid)
    #     if not user:
    #         return jsonify(Error = "User Not Found"), 404
    #
    #     addresses = addressesDao.getAddressesByUserId(sid)
    #     result_list=[]
    #     for row in addresses:
    #         address = Address().build_dict_from_row(row)
    #         result_list.append(address)
    #     return jsonify(Addresses=result_list)
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
                return jsonify(Requester=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post requester"), 400

    def insertRequest(self, form, nid):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
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

    def getRequestsByNid(self, nid):
        dao = RequestersDAO()
        row = dao.getRequesterById(nid)
        if not row:
            return jsonify(Error="Requester Not Found"), 404
        else:
            dao2 = ResourceRequestsDAO()
            requests_list = dao2.getRequestsByNid(nid)
            result_list = []
            for row in requests_list:
                request = ResourceRequest().build_dict_from_row_resource(row)
                result_list.append(request)
            return jsonify(Requests=result_list)
