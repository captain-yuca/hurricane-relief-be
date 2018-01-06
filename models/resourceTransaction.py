class ResourceTransaction:

    def build_dict_from_row(self, row):
        result = {}
        result['tid'] = row[0]
        result['transaction_amount'] = row[1]
        result['sid'] = row[2] #Foreign Key from Supplier
        result['supplier_payment_info'] = row[3] #Foreign Key from PaymentInfo
        result['purchase_id'] = row[4] #Foreign Key from Purchase
        return result
