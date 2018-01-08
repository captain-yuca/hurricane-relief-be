from models.user import User
class Requester:

    def build_dict_from_row(self, row):
        result = {}
        result['nid'] = row[0]
        result['user'] = User().build_dict_from_row(row[1:])
        return result
