from models.user import User
class Supplier:

    def build_dict_from_row(self, row):
        result = {}
        result['sid'] = row[0]
        result['user'] = User().build_dict_from_row(row[0:])
        return result
