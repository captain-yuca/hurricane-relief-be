from models.resource import Resource

class AvailabilityAnnouncement:
    def build_dict_from_row(self, row):
        result = {}
        result['ann_id'] = row[0]
        result['date'] = row[1]
        return result
    def build_dict_from_row_resource(self, row):
        result = {}
        result['ann_id'] = row[0]
        result['date'] = row[1]
        result['resource'] = Resource().build_dict_from_row_category(row[2:])
        return result
