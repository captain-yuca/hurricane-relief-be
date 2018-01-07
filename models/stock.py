from models.resource import Resource
from models.supplier import Supplier
class Stock:

    def build_dict_from_row(self, row):
        result = {}
        result['resource'] = Resource().build_dict_from_row_category(row[0:4])
        result['sid'] = Supplier().build_dict_from_row_region(row[4:10])
        result['currentpriceperitem'] = row[10]
        result['qty'] = row[11]
        return result

    def build_dict_from_row_resource(self, row):
        result = {}
        result['currentpriceperitem'] = row[0]
        result['qty'] = row[1]
        result['resource'] = Resource().build_dict_from_row_category(row[2:])
        return result

    # def build_dict_from_row_supplier(self, row):
    #     result = {}
    #     result['currentpriceperitem'] = row[0]
    #     result['qty'] = row[1]
    #     result['supplier'] = Supplier().build_dict_from_row(row[2:])
    #     return result
