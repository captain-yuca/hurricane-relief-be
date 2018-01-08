from models.requester import Requester
class ResourceRequest:
    def build_dict_from_row(self, row):
        result = {}
        result['req_id'] = row[0]
        result['date'] = row[1]
        result['requester'] = Requester().build_dict_from_row(row[2:])
        return result
