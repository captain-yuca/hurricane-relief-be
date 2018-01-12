from config.dbconfig import url
import psycopg2

class AvailabilityAnnoucementDetailsDAO:

    def __init__(self):
        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )
    def getAllAnnouncementDetails(self):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsById(self, ann_id, rid):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where ann_id = %s and rid = %s;"
        cursor.execute(query, (ann_id, rid))
        result = cursor.fetchone()
        return result

    def getAnnouncementDetailsByAnnidQtyAndPriceattime(self, ann_id, qty, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where ann_id = %s and qty = %s and priceattime = %s;"
        cursor.execute(query, (ann_id, qty, priceattime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByRidQtyAndPriceattime(self, rid, qty, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where rid = %s and qty = %s and priceattime = %s;"
        cursor.execute(query, (rid, qty, priceattime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByAnnidAndQty(self, ann_id, qty):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where ann_id = %s and qty = %s;"
        cursor.execute(query, (ann_id, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByAnnidAndPriceattime(self, ann_id, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where ann_id = %s and priceattime = %s;"
        cursor.execute(query, (ann_id, priceattime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByRidAndQty(self, rid, qty):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where rid = %s and qty = %s;"
        cursor.execute(query, (rid, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByRidAndPriceattime(self, rid, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where rid = %s and priceattime = %s;"
        cursor.execute(query, (rid, priceattime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByQtyAndPriceattime(self, qty, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where qty = %s and priceattime = %s;"
        cursor.execute(query, (qty, priceattime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByAnnid(self, ann_id):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where ann_id = %s;"
        cursor.execute(query, (ann_id, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByRid(self, rid):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where rid = %s;"
        cursor.execute(query, (rid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByQty(self, qty):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where qty = %s;"
        cursor.execute(query, (qty, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByPriceattime(self, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetail where priceattime = %s;"
        cursor.execute(query, (priceattime, ))
        result = []
        for row in cursor:
            result.append(row)
        return result
