from models.resource import Resource

class ResourceTransactionDetails:

    def build_dict_from_row(self, row):
        result = {}
        result['rid'] = row[0] #ResourceId
        result['tid'] = row[1] #TransactionId
        result['qty'] = row[2] #Quantity
        result['purchase_price'] = row[3] #Purchase Price
        return result

    def build_dict_from_row_resource(self, row):
        result = {}
        result['qty'] = row[0] #Quantity
        result['purchase_price'] = row[1] #Purchase Price
        result['resource'] = Resource().build_dict_from_row_category(row[2:])
        return result
