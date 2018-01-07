class AvailabilityAnnouncementDetails:

    def build_dict_from_row(self, row):
        result = {}
        result['ann_id'] = row[0] # Availability Announcement Id
        result['rid'] = row[1] # Resource Id
        result['qty'] = row[2] # Quantity to Announce
        result['priceattime'] = row[3] # Price when announced
        return result