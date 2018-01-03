from flask import jsonify
from dao.resourceTransactions import ResourceTransactionsDAO
from models.resourceTransaction import ResourceTransaction

class ResourceTransactionsHandler:

    def getAllTransactions(self):
        dao = ResourceTransactionsDAO()
        transactions_list = dao.getAllTransactions()
        result_list = []
        for row in transactions_list:
            result = ResourceTransaction().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def getTransactionById(self, tid):
        dao = ResourceTransactionsDAO()
        row = dao.getTransactionById(tid)
        if not row:
            return jsonify(Error = "Resource Transaction Not Found"), 404
        else:
            transaction = ResourceTransaction().build_dict_from_row(row)
            return jsonify(Transaction=transaction)

    def searchTransactions(self, args):
        sid = args.get("sid")
        purchaseid = args.get("purchaseid")
        dao = ResourceTransactionsDAO()
        transactions_list = []
        if(len(args == 2) and sid and purchaseid):
            transactions_list = dao.getTransactionsBySidAndPurchaseid(sid, purchaseid)
        elif(len(args) == 1 and sid):
            transactions_list = dao.getTransactionsBySid(sid)
        elif(len(args) == 1 and purchaseid):
            transactions_list = dao.getTransactionsByPurchaseid(purchaseid)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in transactions_list:
            result = ResourceTransaction().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Transactions = result_list)