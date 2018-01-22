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
            return jsonify(Error="Resource Transaction Not Found"), 404
        else:
            transaction = ResourceTransaction().build_dict_from_table(row)
            return jsonify(Transaction=transaction)

    def searchTransactions(self, args):
        sid = args.get("sid")
        purchaseid = args.get("purchaseid")
        transaction_amount = args.get("transaction_amount")
        supplier_pi_id = args.get("supplier_pi_id")
        dao = ResourceTransactionsDAO()
        transactions_list = []
        if(len(args) == 3) and sid and purchaseid and transaction_amount:
            transactions_list = dao.getTransactionsBySidPurchaseidTransactionAmount(sid, purchaseid, transaction_amount)
        elif(len(args) == 2) and sid and purchaseid:
            transactions_list = dao.getTransactionsBySidAndPurchaseid(sid, purchaseid)
        elif(len(args)==2) and sid and transaction_amount:
            transactions_list = dao.getTransactionsBySidAndTransactionAmount(sid, transaction_amount)
        elif(len(args)==2) and purchaseid and transaction_amount:
            transactions_list = dao.getTransactionsByPurchaseIdAndTransactionAmount(purchaseid, transaction_amount)
        elif(len(args) == 2) and sid and supplier_pi_id:
            transactions_list = dao.getTransactionsBySidAndPaymentInfoId(sid, supplier_pi_id)
        elif(len(args) == 2) and transaction_amount and supplier_pi_id:
            transactions_list = dao.getTransactionsByTransactionAmountAndPaymentInfoId(transaction_amount, supplier_pi_id)
        elif(len(args) == 1) and sid:
            transactions_list = dao.getTransactionsBySid(sid)
        elif(len(args) == 1) and purchaseid:
            transactions_list = dao.getTransactionsByPurchaseid(purchaseid)
        elif(len(args) == 1) and transaction_amount:
            transactions_list = dao.getTransactionsByTransactionAmount(transaction_amount)
        elif(len(args) == 1) and supplier_pi_id:
            transactions_list = dao.getTransactionsByPaymentInfoId(supplier_pi_id)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in transactions_list:
            result = ResourceTransaction().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)
