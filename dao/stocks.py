from config.dbconfig import pg_config
import psycopg2

class StocksDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllStocks(self):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStockById(self, rid, sid):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where rid = %s and sid = %s;"
        cursor.execute(query, (rid, sid))
        result = cursor.fetchone()
        return result

    def getStocksByRidQtysumAndCurrentpriceperitem(self, rid, qtysum, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where rid = %s and qtysum = %s and " \
                "currentpriceperitem = %s;"
        cursor.execute(query, (rid, qtysum, currentpriceperitem))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksBySidQtysumAndCurrentpriceperitem(self, sid, qtysum, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where sid = %s and qtysum = %s " \
                "and currentpriceperitem = %s;"
        cursor.execute(query, (sid, qtysum, currentpriceperitem))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByRidAndQtysum(self, rid, qtysum):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where rid = %s and qtysum = %s;"
        cursor.execute(query, (rid, qtysum))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByRidAndCurrentpriceperitem(self, rid, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where rid = %s and " \
                "currentpriceperitem = %s;"
        cursor.execute(query, (rid, currentpriceperitem))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksBySidAndQtysum(self, sid, qtysum):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where sid = %s and qtysum = %s;"
        cursor.execute(query, (sid, qtysum))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksBySidAndCurrentpriceperitem(self, sid, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where sid = %s and " \
                "currentpriceperitem = %s;"
        cursor.execute(query, (sid, currentpriceperitem))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByQtysumAndCurrentpriceperitem(self, qtysum, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where qtysum = %s and " \
                "currentpriceperitem = %s;"
        cursor.execute(query, (qtysum, currentpriceperitem))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByRid(self, rid):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where rid = %s;"
        cursor.execute(query, (rid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksBySid(self, sid):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where sid = %s;"
        cursor.execute(query, (sid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByQtySum(self, qtysum):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where qtysum = %s;"
        cursor.execute(query, (qtysum, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByCurrentpriceperitem(self, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resources natural inner join categories natural inner join " \
                "suppliers natural inner join users natural inner join address where currentpriceperitem = %s;"
        cursor.execute(query, (currentpriceperitem, ))
        result = []
        for row in cursor:
            result.append(row)
        return result



