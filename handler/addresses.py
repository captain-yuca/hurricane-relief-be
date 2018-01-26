from flask import jsonify
from dao.addresses import AddressesDAO
from models.address import Address

class AddressesHandler:

    def getAllAddresses(self):
        dao = AddressesDAO()
        users_list = dao.getAllAddresses()
        result_list=[]
        for row in users_list:
            address = Address().build_dict_from_row(row)
            result_list.append(address)
        return jsonify(result_list)

    def getAddressById(self, add_id):
        dao = AddressesDAO()
        row = dao.getAddressById(add_id)
        if not row:
            return jsonify(Error = "Address Not Found"), 404
        else:
            address = Address().build_dict_from_row(row)
            return jsonify(address)
