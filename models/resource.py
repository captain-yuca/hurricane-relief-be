class Resource:

    def build_dict_from_row(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['catId'] = row[2] #Foreign Key form Categories
        return result