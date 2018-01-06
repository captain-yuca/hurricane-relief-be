from flask import jsonify
from dao.payment_info import PaymentInfoDAO
from models.payment_info import PaymentInfo

class PaymentInfoHandler:

    def getAllPaymentInfo(self):
        dao = PaymentInfoDAO()
        paymentInfo_list = dao.getAllPaymentInfo()
        result_list=[]
        for row in paymentInfo_list:
            paymentInfo = PaymentInfo().build_dict_from_row(row)
            result_list.append(paymentInfo)
        return jsonify(PaymentInfo=result_list)

    def getPaymentInfoById(self, pi_id):
        dao = PaymentInfoDAO()
        row = dao.getPaymentInfoById(pi_id)
        if not row:
            return jsonify(Error = "Payment Info Not Found"), 404
        else:
            paymentInfo = PaymentInfo().build_dict_from_row(row)
            return jsonify(PaymentInfo = paymentInfo)
