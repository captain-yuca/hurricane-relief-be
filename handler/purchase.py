from flask import jsonify
from dao.purchase import PurchaseDAO
from models.purchase import Purchase

class PurchaseHandler:

    def getAllPurchases(self):
        dao = PurchaseDAO()
        purchases_list = dao.getAllPurchases()
        result_list = []
        for row in purchases_list:
            result = Purchase().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(result_list)

    def getPurchaseById(self, purchase_id):
        dao = PurchaseDAO()
        row = dao.getPurchaseById(purchase_id)
        if not row:
            return jsonify(Error="Resource Purchase Not Found"), 404
        else:
            purchase = Purchase().build_dict_from_table(row)
            return jsonify(purchase)

    def getAllReserves(self):
        dao = PurchaseDAO()
        purchases_list = dao.getAllReserves()
        result_list = []
        for row in purchases_list:
            result = Purchase().build_dict_from_row3(row)
            result_list.append(result)
        return jsonify(result_list)

    def getAllPaidPurchases(self):
        dao = PurchaseDAO()
        purchases_list = dao.getAllPaidPurchases()
        result_list = []
        for row in purchases_list:
            result = Purchase().build_dict_from_row3(row)
            result_list.append(result)
        return jsonify(result_list)

    def searchPurchases(self, args):
        date = args.get("date")
        total = args.get("total")
        uid = args.get("uid")
        buyer_pi_id = args.get("buyer_pi_id")
        username = args.get("username") #added by Herbert to implement 18
        dao = PurchaseDAO()
        purchases_list = []
        if(len(args) == 4) and date and total and uid and buyer_pi_id:
            purchases_list = dao.getPurchasesByDateTotalUidAndBuyerPaymentInfoId(date, total, uid, buyer_pi_id)
        elif(len(args) == 3) and date and total and uid:
            purchases_list = dao.getPurchasesByDateTotalAndUid(date, total, uid)
        elif(len(args) == 3) and date and total and buyer_pi_id:
            purchases_list = dao.getPurchasesByDateTotalAndBuyerPaymentInfoId(date, total, buyer_pi_id)
        elif(len(args) == 3) and total and uid and buyer_pi_id:
            purchases_list = dao.getPurchasesByTotalUidAndBuyerPaymentInfoId(total, uid, buyer_pi_id)
        elif(len(args) == 3) and date and uid and buyer_pi_id:
            purchases_list = dao.getPurchasesByDateUidAndBuyerPaymentInfoId(date, uid, buyer_pi_id)
        elif(len(args) == 2) and date and total:
            purchases_list = dao.getPurchasesByDateAndTotal(date, total)
        elif(len(args) == 2) and date and uid:
            purchases_list = dao.getPurchasesByDateAndUid(date, uid)
        elif(len(args) == 2) and date and buyer_pi_id:
            purchases_list = dao.getPurchasesByDateAndBuyerPaymentInfo(date, buyer_pi_id)
        elif(len(args) == 2) and total and uid:
            purchases_list = dao.getPurchasesByTotalAndUid(total,uid)
        elif(len(args) == 2) and total and buyer_pi_id:
            purchases_list = dao.getPurchasesByTotalAndBuyerPaymentInfoId(total, buyer_pi_id)
        elif(len(args) == 2) and uid and buyer_pi_id:
            purchases_list = dao.getPurchasesByUidAndBuyerPaymentInfoId(uid, buyer_pi_id)
        elif(len(args) == 1) and date:
            purchases_list = dao.getPurchasesByDate(date)
        elif(len(args) == 1) and total:
            purchases_list = dao.getPurchasesByTotal(total)
        elif(len(args) == 1) and uid:
            purchases_list = dao.getPurchasesByUid(uid)
        elif(len(args) == 1) and buyer_pi_id:
            purchases_list = dao.getPurchasesByBuyerPaymentInfoId(buyer_pi_id)
        #this case added by Herbert to implement 18
        elif(len(args) == 1) and username:
            purchases_list = dao.getPurchasesBySupplier(username)
        else:
            return jsonify(Error="Malformed query string"), 400

        if (len(args) == 1) and buyer_pi_id:
            result_list = []
            for row in purchases_list:
                result = Purchase().build_dict_from_row2(row)
                result_list.append(result)
            return jsonify(result_list)
        else:
            result_list = []
            for row in purchases_list:
                result = Purchase().build_dict_from_row(row)
                result_list.append(result)
            return jsonify(result_list)
