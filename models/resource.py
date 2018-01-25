from models.category import Category
class Resource:

    def build_dict_from_row(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['category'] = Category().build_dict_from_row(row[2:])
        return result

    def build_dict_from_row_category(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['category'] = Category().build_dict_from_row(row[2:])
        return result
