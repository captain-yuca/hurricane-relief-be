from config.dbconfig import pg_config
import psycopg2

class AvailabilityAnnoucementDetailsDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllAnnouncementDetails(self):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsById(self, ann_id, rid):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where ann_id = %s and rid = %s;"
        cursor.execute(query, (ann_id, rid))
        result = cursor.fetchone()
        return result

    def getAnnouncementDetailsByAnnidQtyAndPriceattime(self, ann_id, qty, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where ann_id = %s and qty = %s and priceattime = %s;"
        cursor.execute(query, (ann_id, qty, priceattime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByRidQtyAndPriceattime(self, rid, qty, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where rid = %s and qty = %s and priceattime = %s;"
        cursor.execute(query, (rid, qty, priceattime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByAnnidAndQty(self, ann_id, qty):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where ann_id = %s and qty = %s;"
        cursor.execute(query, (ann_id, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByAnnidAndPriceattime(self, ann_id, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where ann_id = %s and priceattime = %s;"
        cursor.execute(query, (ann_id, priceattime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByRidAndQty(self, rid, qty):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where rid = %s and qty = %s;"
        cursor.execute(query, (rid, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByRidAndPriceattime(self, rid, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where rid = %s and priceattime = %s;"
        cursor.execute(query, (rid, priceattime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByQtyAndPriceattime(self, qty, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where qty = %s and priceattime = %s;"
        cursor.execute(query, (qty, priceattime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByAnnid(self, ann_id):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where ann_id = %s;"
        cursor.execute(query, (ann_id, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByRid(self, rid):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where rid = %s;"
        cursor.execute(query, (rid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByQty(self, qty):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where qty = %s;"
        cursor.execute(query, (qty, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementDetailsByPriceattime(self, priceattime):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncementdetails where priceattime = %s;"
        cursor.execute(query, (priceattime, ))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    
    
    

