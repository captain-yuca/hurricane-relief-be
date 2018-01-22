from flask import jsonify
from dao.users import UsersDAO
from dao.requesters import RequestersDAO

from models.requester import Requester
from models.address import Address

class RequestersHandler:

    def getAllRequesters(self):
        dao = RequestersDAO()
        requesters_list = dao.getAllRequesters()
        result_list=[]
        for row in requesters_list:
            requester = Requester().build_dict_from_row(row)
            result_list.append(requester)
        return jsonify(Requesters=result_list)

    def getRequesterById(self, nid):
        dao = RequestersDAO()
        row = dao.getRequesterById(nid)
        if not row:
            return jsonify(Error = "Requester Not Found"), 404
        else:
            requester = Requester().build_dict_from_row(row)
            return jsonify(Requester = requester)

    def getRequestersCountByRegion(self):
        dao = RequestersDAO()
        counts_list = dao.getRequestersCountByRegion()
        result_list = []
        for row in counts_list:
            count = Address().build_dict_from_row_count(row)
            result_list.append(count)
        return jsonify(requesters_per_region=result_list)

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
