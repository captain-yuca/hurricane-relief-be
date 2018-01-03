class ResourceTransaction:

    def build_dict_from_row(self, row):
        result = {}
        result['tid'] = row[0]
        result['sid'] = row[1] #Foreign Key from Supplier
        result['purchaseid'] = row[2] #Foreign Key from Purchase
        return result
