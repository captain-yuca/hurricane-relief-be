from models.resource import Resource
from models.supplier import Supplier
class ResourceTransaction:

    def build_dict_from_row(self, row):
        result = {}
        result['tid'] = row[0]
        result['transactionammount'] = row[1] #Foreign Key from Supplier

        return result

    def build_dict_from_row_transactions(self, row):
        result = {}
        result['tid'] = row[0]
        result['transactionAmmount'] = row[1]
        result['sid'] = row[2] #Foreign Key from Supplier
        result['qty'] = row[3]
        result['transactionPrice'] = row[4]
        result['resource'] = Resource().build_dict_from_row_category(row[5:])
        return result
    def build_dict_from_table(self, table):
        transaction = {}
        transaction_detail = {}
        isFirstRow = True
        for row in table:
            if isFirstRow: #if creating a transaction for the first time
                transaction = {}
                transaction['transactionId'] = row[0]
                transaction['total'] = row[1]
                transaction['purchaseId'] = row[2]
                transaction['supplier'] = Supplier().build_dict_from_row(row[3:11])
                transaction['details'] = []
                transaction_detail['qty'] = row[11]
                transaction_detail['purchase_price'] = row[12]
                transaction_detail['resource'] = Resource().build_dict_from_row_category(row[13:])
                isFirstRow = False
            else:
                transaction_detail['qty'] = row[11]
                transaction_detail['purchasePrice'] = row[12]
                transaction_detail['resource'] = Resource().build_dict_from_row_category(row[13:])

            transaction['details'].append(transaction_detail)
            transaction_detail = {}
        return transaction
    def build_dict_from_table_no_sup_no_pur(self, table):
        transaction = {}
        transaction_detail = {}
        isFirstRow = True
        for row in table:
            if isFirstRow: #if creating a transaction for the first time
                transaction = {}
                transaction['transactionId'] = row[0]
                transaction['total'] = row[1]
                transaction['details'] = []
                transaction_detail['qty'] = row[11]
                transaction_detail['purchasePrice'] = row[12]
                transaction_detail['resource'] = Resource().build_dict_from_row_category(row[13:])
                isFirstRow = False
            else:
                transaction_detail['qty'] = row[11]
                transaction_detail['purchasePrice'] = row[12]
                transaction_detail['resource'] = Resource().build_dict_from_row_category(row[13:])

            transaction['details'].append(transaction_detail)
            transaction_detail = {}
        return transaction
