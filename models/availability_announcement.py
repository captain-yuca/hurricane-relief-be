from models.resource import Resource
from models.supplier import Supplier
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
    def build_dict_from_table_details(self, table):
        announcement = {}
        announcement_detail = {}
        isFirstRow = True
        for row in table:
            if isFirstRow: #if creating a announcement for the first time
                announcement = {}
                announcement['ann_id'] = row[0]
                announcement['date'] = row[1]
                announcement['supplier'] = Supplier().build_dict_from_row(row[2:11])
                announcement['details'] = []
                announcement_detail['qty'] = row[11]
                announcement_detail['price_at_time'] = row[12]
                announcement_detail['resource'] = Resource().build_dict_from_row_category(row[13:])
                isFirstRow = False
            else:
                announcement_detail['qty'] = row[11]
                announcement_detail['price_at_time'] = row[12]
                announcement_detail['resource'] = Resource().build_dict_from_row_category(row[13:])

            announcement['details'].append(announcement_detail)
            announcement_detail = {}
        return announcement
    def build_dict_from_table(self, table):
        announcements = []
        announcement=None
        announcement_detail = None
        isFirstRow = True
        for row in table:
            if not announcement or announcement['annId']!=row[0]: #if creating a transaction for the first time
                if announcement:
                    announcements.append(announcement)
                announcement = {}
                announcement['annId'] = row[0]
                announcement['sid'] = row[1]
                announcement['annDate'] = row[2]
                announcement['details'] = []
                announcement_detail = {}
                announcement_detail['qty'] = row[3]
                announcement_detail['priceAtTime'] = row[4]
                announcement_detail['resource'] = Resource().build_dict_from_row_category(row[5:])

            else:
                announcement_detail['qty'] = row[3]
                announcement_detail['priceAtTime'] = row[4]
                announcement_detail['resource'] = Resource().build_dict_from_row_category(row[5:])
            announcement['details'].append(announcement_detail)
            announcement_detail = {}

        announcements.append(announcement)
        return announcements
    def build_dict_from_table_no_sup(self, table):
        announcements = []
        announcement=None
        announcement_detail = None
        isFirstRow = True
        for row in table:
            if not announcement or announcement['annId']!=row[0]: #if creating a transaction for the first time
                if announcement:
                    announcements.append(announcement)
                announcement = {}
                announcement['annId'] = row[0]
                announcement['annDate'] = row[1]
                announcement['details'] = []
                announcement_detail = {}
                announcement_detail['qty'] = row[2]
                announcement_detail['priceAtTime'] = row[3]
                announcement_detail['resource'] = Resource().build_dict_from_row_category(row[4:])

            else:
                announcement_detail['qty'] = row[2]
                announcement_detail['priceAtTime'] = row[3]
                announcement_detail['resource'] = Resource().build_dict_from_row_category(row[4:])
            announcement['details'].append(announcement_detail)
            announcement_detail = {}

        announcements.append(announcement)
        return announcements
