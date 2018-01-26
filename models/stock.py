from models.resource import Resource
from models.supplier import Supplier
class Stock:

    def build_dict_from_row(self, row):
        result = {}
        result['resource'] = Resource().build_dict_from_row_category(row[0:4])
        result['supplier'] = Supplier().build_dict_from_row_region(row[4:10])
        result['currentPricePerItem'] = row[10]
        result['qty'] = row[11]
        return result

    def build_dict_from_row_resource(self, row):
        result = {}
        result['currentPricePerItem'] = row[0]
        result['qty'] = row[1]
        result['resource'] = Resource().build_dict_from_row_category(row[2:])
        return result

    def build_dict_from_row_sum(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['qtySum'] = row[2]
        return result

    def build_dict_from_row_no_supplier(self, row):
        result = {}
        result['resource'] = Resource().build_dict_from_row_category(row[0:4])
        result['currentPricePerItem'] = row[4]
        result['qty'] = row[5]
        return result
