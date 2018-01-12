from config.dbconfig import url
import psycopg2

class ResourceRequestDetailsDAO:

    def __init__(self):
        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )
    def getAllRequestDetails(self):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetail;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsById(self, req_id, rid):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetail where req_id = %s and rid = %s;"
        cursor.execute(query, (req_id, rid))
        result = cursor.fetchone()
        return result

    def getRequestDetailsByReqidAndQty(self, req_id, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetail where req_id = %s and qty = %s;"
        cursor.execute(query, (req_id, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRisAndQty(self, rid, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcerequestdetail where rid = %s and qty = %s;"
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
