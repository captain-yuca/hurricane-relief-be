from models.payment_info import PaymentInfo
class Purchase:

    def build_dict_from_row(self, row):
        result = {}
        result['purchase_id'] = row[0]
        result['date'] = row[1] #Purchase Date
        result['total'] = row[2] #Purchase Total
        result['uid'] = row[3] #User Id, Buyer (Foreign Key)
        result['buyer_pi_id'] = row[4] #Buyer Payment Info (Foreign Key)
        return result

    def build_dict_from_row_payment(self, row):
        result = {}
        result['purchase_id'] = row[0]
        result['date'] = row[1] #Purchase Date
        result['total'] = row[2] #Purchase Total
        result['uid'] = row[3] #User Id, Buyer (Foreign Key)
        result['payment_info'] = PaymentInfo().build_dict_from_row(row[4:])
        return result
    def build_dict_from_row2(self, row):
        result = {}
        result['purchase_id'] = row[0]
        result['tid'] = row[1]
        result['rname'] = row[2]
        result['catname'] = row[3]
        result['purchaseprice'] = row[4]
        result['transactionammount'] = row[5]
        result['purchase_date'] = row[6]
        return result
