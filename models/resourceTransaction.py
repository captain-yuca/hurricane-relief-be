from models.resource import Resource
class ResourceTransaction:

    def build_dict_from_row(self, row):
        result = {}
        result['tid'] = row[0]
        result['transaction_amount'] = row[1]
        result['sid'] = row[2] #Foreign Key from Supplier
        result['supplier_payment_info'] = row[3] #Foreign Key from PaymentInfo
        result['purchase_id'] = row[4] #Foreign Key from Purchase

        return result

    def build_dict_from_row_transactions(self, row):
        result = {}
        result['tid'] = row[0]
        result['transaction_amount'] = row[1]
        result['sid'] = row[2] #Foreign Key from Supplier
        result['qty'] = row[3]
        result['purchase_price'] = row[4]
        result['resource'] = Resource().build_dict_from_row_category(row[5:])
        return result
