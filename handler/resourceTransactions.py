from flask import jsonify
from dao.resourceTransactions import ResourceTransactionsDAO
from dao.resourceTransactionDetails import ResourceTransactionDetailsDAO
from dao.suppliers import SuppliersDAO
from dao.resources import ResourcesDAO
from dao.stocks import StocksDAO
from dao.purchase import PurchaseDAO
from dao.payment_info import PaymentInfoDAO
from dao.users import UsersDAO
from models.resourceTransaction import ResourceTransaction
import time

class ResourceTransactionsHandler:

    def getAllTransactions(self):
        dao = ResourceTransactionsDAO()
        transactions_list = dao.getAllTransactions()
        result_list = []
        for row in transactions_list:
            result = ResourceTransaction().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(result_list)

    def getTransactionById(self, tid):
        dao = ResourceTransactionsDAO()
        row = dao.getTransactionById(tid)
        if not row:
            return jsonify(Error="Resource Transaction Not Found"), 404
        else:
            transaction = ResourceTransaction().build_dict_from_table(row)
            return jsonify(transaction)

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
        return jsonify(result_list)

    def checkIfExists(self, supplier_resource_array, sid, rid):
        for entry in supplier_resource_array:
            if entry['sid'] == sid and entry['rid'] == rid:
                return True
        return False



    def insert(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            # VALIDATION
            # TODO: Check if supplier piid is the same
            # TODO: Check if valid objects in details array

            # Check if payment is valid
            buyer_pi_id = PaymentInfoDAO().getPaymentInfoById(form['pi_id'])[0]
            if not buyer_pi_id:
                return jsonify(Error="Purchase Info not found"), 400

            supplier_resource_array = []
            try:
                transaction_details = sorted(form['transactions'], key=lambda k: k['sid'])
            except:
                return jsonify(Error="Malformed post request"), 400

            for detail in transaction_details:
                sid = detail['sid']
                rid = detail['rid']
                qty = detail['qty']
                # Create function
                # Check if supplier and resource key is repeated
                if not self.checkIfExists(supplier_resource_array, sid, rid):

                    # Check if supplier exists
                    if not SuppliersDAO().getSupplierById(sid):
                        return jsonify(Error="Supplier not found"), 400

                    # Check if resource exists
                    if not ResourcesDAO().getResourceById(rid):
                        return jsonify(Error="Resource not found"), 400

                    # Check if qty is valid
                    # Check if stock exists
                    available_stock = StocksDAO().getStockQtyById(rid, sid)
                    if not available_stock:
                        return jsonify(Error="Resource not in stock"), 400

                    # Check if qty is sufficient
                    if available_stock[0] < qty:
                        return jsonify(Error="Resource not enough quantity"), 400

                    supplier_resource_array.append({'sid':detail['sid'], 'rid':detail['rid']})

                else:
                    return jsonify(Error="Repeated"), 400

            user_id = UsersDAO().getUserIdByPIID(buyer_pi_id)

            # Create Purchase
            purchase_id = PurchaseDAO().insert(user_id, buyer_pi_id, 0, time.strftime("%Y/%m/%d"))
            current_sid = None
            current_transaction = None
            purchase_total = 0
            transaction_total = 0

            for detail in transaction_details:
                sid = detail['sid']
                rid = detail['rid']
                qty = detail['qty']
                if not current_sid or current_sid != sid:
                    # TODO: SUPPLIER PI ID
                    pi_id = PaymentInfoDAO().getPaymentInfoBySid(sid)
                    print(current_transaction)
                    if current_transaction:
                        # Update transaction
                        print('hello')
                        ResourceTransactionsDAO().updateTransactionAmmount(current_transaction[0], transaction_total)

                    # Create Transaction
                    current_transaction = ResourceTransactionsDAO().insert(sid, 0, purchase_id, pi_id)
                    print(current_transaction)
                    transaction_total = 0

                # GET the current stock
                current_stock = StocksDAO().getStockQtyById(rid, sid)[0]
                # GET the current price
                current_price = StocksDAO().getStockPriceById(rid, sid)[0]

                # Create Transaction Detail
                ResourceTransactionDetailsDAO().insert(current_transaction, rid, current_price, qty)



                # Subtract Stock
                new_qty = current_stock - qty

                StocksDAO().updateQty(sid, rid, new_qty)
                purchase_total = purchase_total + current_price*qty
                transaction_total = transaction_total + current_price*qty

            # Modify Purchase Total
            PurchaseDAO().updatePurchasePrice(purchase_id, purchase_total)

            ResourceTransactionsDAO().updateTransactionAmmount(current_transaction[0], transaction_total)

            return jsonify({"purchase_id":purchase_id})
