from models.requester import Requester
class ResourceRequest:
    def build_dict_from_row(self, row):
        result = {}
        result['req_id'] = row[0]
        result['date'] = row[1]
        result['requester'] = Requester().build_dict_from_row(row[2:])
        return result
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