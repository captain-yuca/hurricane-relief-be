from models.resource import Resource
from models.supplier import Supplier
class ResourceTransaction:

    def build_dict_from_row(self, row):
        result = {}
        result['tid'] = row[0]
        result['sid'] = row[1]
        result['transactionammount'] = row[2] #Foreign Key from Supplier
        result['purchase_id'] = row[3] #Foreign Key from PaymentInfo
        result['supplier_pi_id'] = row[4] #Foreign Key from Purchase

        return result

    def build_dict_from_row_transactions(self, row):
        result = {}
        result['tid'] = row[0]
        result['transaction_amount'] = row[1]
        result['sid'] = row[2] #Foreign Key from Supplier
        result['qty'] = row[3]
        result['transaction_price'] = row[4]
        result['resource'] = Resource().build_dict_from_row_category(row[5:])
        return result
    def build_dict_from_table(self, table):
        transaction = {}
        transaction_detail = {}
        isFirstRow = True
        for row in table:
            if isFirstRow: #if creating a transaction for the first time
                transaction = {}
                transaction['transaction_id'] = row[0]
                transaction['total'] = row[1]
                transaction['purchase_id'] = row[2]
                transaction['supplier'] = Supplier().build_dict_from_row(row[3:9])
                transaction['details'] = []
                transaction_detail['qty'] = row[9]
                transaction_detail['purchase_price'] = row[10]
                transaction_detail['resource'] = Resource().build_dict_from_row_category(row[11:])
                isFirstRow = False
            else:
                transaction_detail['qty'] = row[8]
                transaction_detail['purchase_price'] = row[9]
                transaction_detail['resource'] = Resource().build_dict_from_row_category(row[10:])

            transaction['details'].append(transaction_detail)
            transaction_detail = {}
        return transaction
