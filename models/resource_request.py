from models.requester import Requester
from models.resource import Resource
class ResourceRequest:
    def build_dict_from_row(self, row):
        result = {}
        result['req_id'] = row[0]
        result['date'] = row[1]
        result['requester'] = Requester().build_dict_from_row(row[2:])
        return result
    def build_dict_from_table_resources(self, table):
        result_list=[]
        request = {}
        request_detail = {}
        for row in table:
            if request.get('req_id') != None and request['req_id'] == row[0]: #if creating a request for the first time
                request_detail['qty'] = row[9]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[10:])
                request['details'].append(request_detail)
            else:
                if request.get('req_id') != None:
                    result_list.append(request)

                request = {}
                request['req_id'] = row[0]
                request['date'] = row[1]
                request['requester'] = Requester().build_dict_from_row(row[2:9])
                request['details'] = []
                request_detail['qty'] = row[9]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[10:])

            request['details'].append(request_detail)
            request_detail = {}


        return result_list
