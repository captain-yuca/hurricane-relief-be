from models.requester import Requester
from models.resource import Resource
class ResourceRequest:
    def build_dict_from_row(self, row):
        result = {}
        result['req_id'] = row[0]
        result['date'] = row[1]
        result['requester'] = Requester().build_dict_from_row(row[2:])
        return result

    def build_dict_from_row_resource(self, row):
        result = {}
        result['req_id'] = row[0]
        result['date'] = row[1]
        result['resource'] = Resource().build_dict_from_row_category(row[2:])
        return result

    def build_dict_from_table_details(self, table):
        request = {}
        request_detail = {}
        isFirstRow = True
        for row in table:
            if isFirstRow: #if creating a request for the first time
                request = {}
                request['req_id'] = row[0]
                request['date'] = row[1]
                request['requester'] = Requester().build_dict_from_row(row[2:9])
                request['details'] = []
                request_detail['qty'] = row[9]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[10:])
                request_detail['qty'] = row[9]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[10:])
                isFirstRow = False
            else:
                request_detail['qty'] = row[9]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[10:])

            request['details'].append(request_detail)
            request_detail = {}


        return request
