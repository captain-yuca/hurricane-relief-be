from flask import jsonify
from dao.users import UsersDAO
from dao.suppliers import SuppliersDAO

from models.supplier import Supplier

class SuppliersHandler:

    def getAllSuppliers(self):
        dao = SuppliersDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list=[]
        for row in suppliers_list:
            supplier = Supplier().build_dict_from_row(row)
            result_list.append(supplier)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, sid):
        dao = SuppliersDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            supplier = Supplier().build_dict_from_row(row)
            return jsonify(Supplier = supplier)

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
