from models.payment_info import PaymentInfo
from models.user import User
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
    def build_dict_from_row3(self, row):
        result = {}
        result['purchase_id'] = row[0]
        result['tid'] = row[1]
        result['rname'] = row[2]
        result['catname'] = row[3]
        result['purchaseprice'] = row[4]
        result['transactionammount'] = row[5]
        result['purchase_date'] = row[6]
        result['supplier'] = row[7]
        result['buyer'] = row[8]
        return result
    def build_dict_from_table(self, table):
        purchase = {}
        purchase_detail = {}
        isFirstRow = True
        for row in table:
            if isFirstRow: #if creating a purchase for the first time
                purchase = {}
                purchase['purchase_id'] = row[0]
                purchase['date'] = row[1]
                purchase['total'] = row[2]
                purchase['user'] = User().build_dict_from_row_noAdmin(row[3:])
                purchase['payment_info'] = PaymentInfo().build_dict_from_row(row[8:])
                purchase['transactions'] = []
                purchase_detail['tid'] = row[11]
                purchase_detail['sid'] = row[12]
                purchase_detail['qty'] = row[13]
                isFirstRow = False
            else:
                purchase_detail['tid'] = row[11]
                purchase_detail['sid'] = row[12]
                purchase_detail['qty'] = row[13]

            purchase['transactions'].append(purchase_detail)
            purchase_detail = {}


        return purchase
