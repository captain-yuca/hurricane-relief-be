from flask import jsonify
from dao.users import UsersDAO
from dao.addresses import AddressesDAO
from models.user import User
from models.address import Address

class UsersHandler:

    def getAllUsers(self):
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        result_list=[]
        for row in users_list:
            user = User().build_dict_from_row(row)
            result_list.append(user)
        return jsonify(Users=result_list)

    def getUserById(self, uid):
        dao = UsersDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = User().build_dict_from_row(row)
            return jsonify(User = user)

    def getAddressesByUserId(self, uid):
        userDao = UsersDAO()
        addressesDao = AddressesDAO()
        user = userDao.getUserById(uid)
        if not user:
            return jsonify(Error = "User Not Found"), 404

        addresses = addressesDao.getAddressesByUserId(uid)
        result_list=[]
        for row in addresses:
            address = Address().build_dict_from_row(row)
            result_list.append(address)
        return jsonify(Addresses=result_list)

    def searchUsers(self, args):
        allowedKeys= {"fname", "lname", "username", "isAdmin", "add_id"}
        for key in args.keys():
            if key not in allowedKeys:
                return jsonify(Error="Malformed query string"), 400
            
        dao = UsersDAO()
        users_list = dao.getUsersByParameters(args)
        result_list=[]
        for row in users_list:
            user = User().build_dict_from_row(row)
            result_list.append(user)
        return jsonify(Users=result_list)
