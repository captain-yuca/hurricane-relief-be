class Purchase:

    def build_dict_from_row(self, row):
        result = {}
        result['purchase_id'] = row[0]
        result['date'] = row[1] #Purchase Date
        result['total'] = row[2] #Purchase Total
        result['uid'] = row[3] #User Id, Buyer (Foreign Key)
        result['buyer_pi_id'] = row[4] #Buyer Payment Info (Foreign Key)
        return result