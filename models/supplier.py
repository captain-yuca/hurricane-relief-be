from models.user import User
from models.category import Category
from models.resource import Resource
# from models.stock import Stock
class Supplier:

    def build_dict_from_row(self, row):
        result = {}
        result['sid'] = row[0]
        result['user'] = User().build_dict_from_row_noAdmin(row[1:]) # Changed this to noAdmin -Kelvin
        return result

    def build_dict_from_row_stock(self, row):
        result = {}
        result['sid'] = row[0]
        result['user'] = User().build_dict_from_row_noAdmin(row[1:])          # Changed the 7 to a 6 to comply with the noAdmin
        # result['stock'] = Stock().build_dict_from_row_resource(row[6:])
        return result

    def build_dict_from_row_region(self, row):
        result = {}
        result['sid'] = row[0]
        result['user'] = User().build_dict_from_row_region(row[1:])
        return result
