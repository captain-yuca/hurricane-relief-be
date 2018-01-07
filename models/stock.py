from models.resource import Resource
class Stock:

    def build_dict_from_row(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['currentpriceperitem'] = row[2]
        result['qty'] = row[3]
        return result

    def build_dict_from_row_resource(self, row):
        result = {}
        result['currentpriceperitem'] = row[0]
        result['qty'] = row[1]
        result['resource'] = Resource().build_dict_from_row_category(row[2:])
        return result
