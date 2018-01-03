class Category:

    def build_dict_from_row(self, row):
        result = {}
        result['catId'] = row[0]
        result['catName'] = row[1]
        return result