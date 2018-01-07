class Stock:

    def build_dict_from_row(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['currentpriceperitem'] = row[2]
        result['qty'] = row[3]
        return result