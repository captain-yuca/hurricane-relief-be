from config.dbconfig import pg_config
import psycopg2

class StocksDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllStocks(self):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStockById(self, rid, sid):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where rid = %s and sid = %s;"
        cursor.execute(query, (rid, sid))
        result = cursor.fetchone()
        return result

    def getStocksByRidQtysumAndCurrentpriceperitem(self, rid, qtysum, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where rid = %s and qtysum = %s and " \
                "currentpriceperitem = %s;"
        cursor.execute(query, (rid, qtysum, currentpriceperitem))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksBySidQtysumAndCurrentpriceperitem(self, sid, qtysum, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where sid = %s and qtysum = %s " \
                "and currentpriceperitem = %s;"
        cursor.execute(query, (sid, qtysum, currentpriceperitem))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByRidAndQtysum(self, rid, qtysum):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where rid = %s and qtysum = %s;"
        cursor.execute(query, (rid, qtysum))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByRidAndCurrentpriceperitem(self, rid, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where rid = %s and " \
                "currentpriceperitem = %s;"
        cursor.execute(query, (rid, currentpriceperitem))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksBySidAndQtysum(self, sid, qtysum):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where sid = %s and qtysum = %s;"
        cursor.execute(query, (sid, qtysum))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksBySidAndCurrentpriceperitem(self, sid, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where sid = %s and " \
                "currentpriceperitem = %s;"
        cursor.execute(query, (sid, currentpriceperitem))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByQtysumAndCurrentpriceperitem(self, qtysum, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where qtysum = %s and " \
                "currentpriceperitem = %s;"
        cursor.execute(query, (qtysum, currentpriceperitem))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getStocksByRid(self, rid):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where rid = %s;"
        cursor.execute(query, (rid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksBySid(self, sid):
        cursor = self.conn.cursor()
        query = """
        select currentpriceperitem, qtysum, rid, rname, catid, catname
        from supplier natural join appuser natural join stock natural join resource natural join category
        where sid=%s
        """

        cursor.execute(query, (sid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByQtySum(self, qtysum):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where qtysum = %s;"
        cursor.execute(query, (qtysum, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByCurrentpriceperitem(self, currentpriceperitem):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where currentpriceperitem = %s;"
        cursor.execute(query, (currentpriceperitem, ))
        result = []
        for row in cursor:
            result.append(row)
        return result
    #added by Herbert to search stock using actual names instead of ids
    def getStockByResourceAndUser(self, resource, user):
        cursor = self.conn.cursor()
        query = "select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem, " \
                "qtysum from stock natural inner join resource natural inner join category natural inner join " \
                "supplier natural inner join appuser natural inner join address where rname= %s and username = %s"
        cursor.execute(query, (resource, user,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    #added by herbert to satisfy "see all resource that are in stock with stock>0 and srotby"
    def getStocksInStock(self):
        cursor = self.conn.cursor()
        query = """
                select rid, rname, catId, catName, sid, uid, username, lname, fname, isAdmin, region, currentpriceperitem,
                qtysum from stock natural inner join resource natural inner join category natural inner join
                supplier natural inner join appuser natural inner join address where qtysum>0
                order by rname;
                """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStocksByParams(self, args, max_args, min_args):
        cursor = self.conn.cursor()


        query ="""
        select rid, rname, catId, catName, sid, uid, username, lname, fname, region, currentpriceperitem,
        qtysum from stock natural inner join resource natural inner join category natural inner join
        supplier natural inner join appuser natural inner join address
        where
        """

        selection_length = len(args) + len(max_args) + len(min_args)

        i = 0

        # Go through each args list (args, max_args, min_args) and append the key with its appropiate operator
        # and value. 'i' keeps track of when to stop appending AND to the query.
        for key in min_args.keys():
            if i == selection_length - 1:
                query+= key + " >= %s"
            else:
                query+= key + " >= %s AND "
                i+=1
        for key in max_args.keys():
            if i == selection_length - 1:
                query+= key + " < %s"
            else:
                query+= key + " < %s AND "
                i+=1
        for key in args.keys():
            if i == selection_length - 1:
                query+= key + " = %s"
            else:
                query+= key + " = %s AND "
                i+=1

        args_tuple = tuple(min_args.values()) + tuple(max_args.values()) + tuple(args.values())
        cursor.execute(query, args_tuple)
        result=[]
        for row in cursor:
            result.append(row)
        return result
