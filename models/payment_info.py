class PaymentInfo:

    def build_dict_from_row(self, row):
        result = {}
        result['pi_id'] = row[0]
        result['ccnumber'] = row[1]
        result['exp_date'] = row[2]
        return result
