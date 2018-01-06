class ResourceRequestDetails:

    def build_dict_from_row(self, row):
        result = {}
        result['req_id'] = row[0] # Requester Id
        result['rid'] = row[1] # Resource Id
        result['qty'] = row[2] # Quantity
        return result