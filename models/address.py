class Address:

    def build_dict_from_row(self, row):
        result = {}
        result['add_id'] = row[0]
        result['address1'] = row[1]
        result['address2'] = row[2]
        result['zipcode'] = row[3]
        result['region'] = row[4]
        result['country'] = row[5]
        result['city'] = row[6]
        return result
