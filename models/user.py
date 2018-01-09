from models.address import Address

class User:

    def build_dict_from_row(self, row):
        result = {}
        result['uid'] = row[0]
        result['username'] = row[1]
        result['lastName'] = row[2]
        result['firstName'] = row[3]
        result['isAdmin'] = row[4]
        result['add_id'] = row[5]
        return result

    def build_dict_from_row_noAdmin(self, row): # ADDED THIS DICT WITHOUT ISADMIN
        result = {}
        result['uid'] = row[0]
        result['username'] = row[1]
        result['lastName'] = row[2]
        result['firstName'] = row[3]
        result['add_id'] = row[4]
        return result

    def build_dict_from_row_address(self, row):
        result = {}
        result['uid'] = row[0]
        result['username'] = row[1]
        result['lastName'] = row[2]
        result['firstName'] = row[3]
        result['address'] = Address().build_dict_from_row(row[4:])

    def build_dict_from_row_region(self, row):
        result = {}
        result['uid'] = row[0]
        result['username'] = row[1]
        result['lastName'] = row[2]
        result['firstName'] = row[3]
        result['region'] = row[4]