from flask import jsonify
from dao.resourceTransactionDetails import ResourceTransactionDetailsDAO
from models.resourceTransactionDetails import ResourceTransactionDetails

class ResourceTransactionDetailsHandler:

    def getAllTransactionDetails(self):
        dao = ResourceTransactionDetailsDAO()
        transactionDetails_list = dao.getAllTransactionDetails()
        result_list = []
        for row in transactionDetails_list:
            result = ResourceTransactionDetails().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(result_list)

    def getTransactionDetailsById(self, rid, tid):
        dao = ResourceTransactionDetailsDAO()
        row = dao.getTransactionDetailsById(rid, tid)
        if not row:
            return jsonify(Error="Resource Transaction Detail Not Found"), 404
        else:
            transactionDetail = ResourceTransactionDetails().build_dict_from_row(row)
            return jsonify(transactionDetail)

    def searchTransactionDetails(self, args):
        rid = args.get("rid")
        tid = args.get("tid")
        qty = args.get("qty")
        purchaseprice = ("purchaseprice")
        dao = ResourceTransactionDetailsDAO()
        transactionDetails_list = []
        if(len(args) == 3) and rid and purchaseprice and qty:
            transactionDetails_list = dao.getTransactionDetailsByRidPurchasePriceAndQty(rid, purchaseprice, qty)
        elif(len(args) == 3) and tid and purchaseprice and qty:
            transactionDetails_list = dao.getTransactionDetailsByTidPurchasePriceAndQty(tid, purchaseprice, qty)
        elif(len(args) == 2) and rid and purchaseprice:
            transactionDetails_list = dao.getTransactionDetailsByRidAndPurchasePrice(rid, purchaseprice)
        elif(len(args) == 2) and tid and purchaseprice:
            transactionDetails_list = dao.getTransactionDetailsByTidAndPurchasePrice(tid, purchaseprice)
        elif(len(args) == 2) and rid and qty:
            transactionDetails_list = dao.getTransactionDetailsByRidAndQty(rid, qty)
        elif(len(args) == 2) and tid and qty:
            transactionDetails_list = dao.getTransactionDetailsByTidAndQty(tid, qty)
        elif(len(args) == 2) and purchaseprice and qty:
            transactionDetails_list = dao.getTransactionDetailsByPurchasePriceAndQty(purchaseprice, qty)
        elif(len(args) == 1) and rid:
            transactionDetails_list = dao.getTransactionDetailsByRid(rid)
        elif(len(args) == 1) and tid:
            transactionDetails_list = dao.getTransactionDetailsByTid(tid)
        elif(len(args) == 1) and qty:
            transactionDetails_list = dao.getTransactionDetailsByQty(qty)
        elif(len(args) == 1) and purchaseprice:
            transactionDetails_list = dao.getTransactionDetailsByPurchasePrice(purchaseprice)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in transactionDetails_list:
            result = ResourceTransactionDetails().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(result_list)
