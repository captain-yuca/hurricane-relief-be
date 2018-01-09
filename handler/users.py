from flask import jsonify
from dao.users import UsersDAO
from dao.addresses import AddressesDAO
from dao.purchase import PurchaseDAO
from dao.resourceTransactions import ResourceTransactionsDAO
from models.user import User
from models.address import Address
from models.purchase import Purchase
from models.resourceTransaction import ResourceTransaction

class UsersHandler:

    def getAllUsers(self):
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        result_list=[]
        for row in users_list:
            user = User().build_dict_from_row_noAdmin(row) #CHANGED DICT TO NOADMIN -Kelvin
            result_list.append(user)
        return jsonify(Users=result_list)

    def getUserById(self, uid):
        dao = UsersDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = User().build_dict_from_row_noAdmin(row)
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

    def getPurchasesByUserId(self, uid):
        userDao = UsersDAO()
        purchasesDao = PurchaseDAO()
        user = userDao.getUserById(uid)
        if not user:
            return jsonify(Error = "User Not Found"), 404

        purchases = purchasesDao.getPurchasesByUid(uid)
        result_list=[]
        for row in purchases:
            purchase =Purchase().build_dict_from_row_payment(row)
            result_list.append(purchase)
        return jsonify(purchases=result_list)

    def getUserPurchaseById(self, uid, pi_id):
        userDao = UsersDAO()
        purchasesDao = PurchaseDAO()
        user = userDao.getUserById(uid)
        if not user:
            return jsonify(Error = "User Not Found"), 404

        purchase = purchasesDao.getPurchaseById(pi_id)
        if not purchase or purchase[3]  != uid:
            return jsonify(Error = "Purchase Not Found"), 404

        result = Purchase().build_dict_from_row_payment(purchase)
        return jsonify(purchase=result)

    def getPurchaseDetailsById(self, uid, pi_id):
        userDao = UsersDAO()
        purchasesDao = PurchaseDAO()
        user = userDao.getUserById(uid)
        if not user:
            return jsonify(Error = "User Not Found"), 404

        purchase = purchasesDao.getPurchaseById(pi_id)
        if not purchase or purchase[3]  != uid:
            return jsonify(Error = "Purchase Not Found"), 404

        detailsDao = ResourceTransactionsDAO()
        details_list = detailsDao.getTransactionsByPurchaseid(pi_id)
        result_list = []

        for row in details_list:
            detail = ResourceTransaction().build_dict_from_row_transactions(row)
            result_list.append(detail)
        return jsonify(details=result_list)




    #TOOK OUT ISADMIN HERE AND CHANGED DICT -KELVIN

    def searchUsers(self, args):
        allowedKeys= {"fname", "lname", "username", "add_id"}
        for key in args.keys():
            if key not in allowedKeys:
                return jsonify(Error="Malformed query string"), 400

        dao = UsersDAO()
        users_list = dao.getUsersByParameters(args)
        result_list=[]
        for row in users_list:
            user = User().build_dict_from_row_noAdmin(row)
            result_list.append(user)
        return jsonify(Users=result_list)
