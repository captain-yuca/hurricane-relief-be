class User:

    def build_dict_from_row(self, row):
        result = {}
        result['uid'] = row[0]
        result['username'] = row[1]
        result['firstName'] = row[2]
        result['lastName'] = row[3]
        result['isAdmin'] = row[4]
        return result
