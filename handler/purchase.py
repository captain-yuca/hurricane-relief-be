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
        return jsonify(Purchases=result_list)

    def getPurchaseById(self, purchase_id):
        dao = PurchaseDAO()
        row = dao.getPurchaseById(purchase_id)
        if not row:
            return jsonify(Error="Resource Purchase Not Found"), 404
        else:
            purchase = Purchase().build_dict_from_row(row)
            return jsonify(Purchase=purchase)

    def searchPurchases(selfs, args):
        date = args.get("date")
        total = args.get("total")
        uid = args.get("uid")
        buyer_pi_id = args.get("buyer_pi_id")
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
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in purchases_list:
            result = Purchase().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Purchases=result_list)