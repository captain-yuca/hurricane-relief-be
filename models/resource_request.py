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
        result['qty'] = row[2]
        result['resource'] = Resource().build_dict_from_row_category(row[3:])
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
                request['requester'] = Requester().build_dict_from_row(row[2:10])
                request['details'] = []
                request_detail['qty'] = row[10]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[11:])
                isFirstRow = False
            else:
                request_detail['qty'] = row[10]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[11:])

            request['details'].append(request_detail)
            request_detail = {}


        return request

    def build_dict_from_row2(self, row): #created by Herbert to work for new DAO method getRequestedResources
        result = {}
        result['req_id'] = row[0]
        result['rid'] = row[1]
        result['rname'] = row[2]
        result['catname'] = row[3]
        result['qty'] = row[4]
        result['nid'] = row[5]
        result['uid'] = row[6]
        result['username'] = row[7]
        result['lname'] = row[8]
        result['fname'] = row[9]
        result['add_id'] = row[10]
        result['re1_date'] = row[11]
        return result
    def build_dict_from_table(self, table):
        requests = []
        request=None
        request_detail = None
        isFirstRow = True
        for row in table:
            if not request or request['reqId']!=row[0]: #if creating a transaction for the first time
                if request:
                    requests.append(request)
                request = {}
                request['reqId'] = row[0]
                request['nid'] = row[1]
                request['reqDate'] = row[2]
                request['details'] = []
                request_detail = {}
                request_detail['qty'] = row[3]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[4:])

            else:
                request_detail['qty'] = row[3]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[4:])
            request['details'].append(request_detail)
            request_detail = {}

        requests.append(request)
        return requests

    def build_dict_from_table_no_nid(self, table):
        requests = []
        request=None
        request_detail = None
        isFirstRow = True
        for row in table:
            if not request or request['reqId']!=row[0]: #if creating a transaction for the first time
                if request:
                    requests.append(request)
                request = {}
                request['reqId'] = row[0]
                request['reqDate'] = row[1]
                request['details'] = []
                request_detail = {}
                request_detail['qty'] = row[2]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[3:])

            else:
                request_detail['qty'] = row[2]
                request_detail['resource'] = Resource().build_dict_from_row_category(row[3:])
            request['details'].append(request_detail)
            request_detail = {}

        requests.append(request)
        return requests
