from config.dbconfig import pg_config
import psycopg2

class ResourceRequestDetailsDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllRequestDetails(self):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetails;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsById(self, req_id, rid):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetails where req_id = %s and rid = %s;"
        cursor.execute(query, (req_id, rid))
        result = cursor.fetchone()
        return result

    def getRequestDetailsByReqidAndQty(self, req_id, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetails where req_id = %s and qty = %s;"
        cursor.execute(query, (req_id, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRisAndQty(self, rid, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetails where rid = %s and qty = %s;"
        cursor.execute(query, (rid, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByReqid(self, req_id):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetail where req_id = %s;"
        cursor.execute(query, (req_id, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRid(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetail where rid = %s;"
        cursor.execute(query, (rid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByQty(self, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetail where qty = %s;"
        cursor.execute(query, (qty, ))
        result = []
        for row in cursor:
            result.append(row)
        return result
