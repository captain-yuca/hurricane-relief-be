from config.dbconfig import url
import psycopg2

class ResourceTransactionDetailsDAO:

    def __init__(self):

        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )

    def getAllTransactionDetails(self):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail;"
        cursor.execute(query)
        result= []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsById(self, rid, tid):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where rid = %s and tid = %s;"
        cursor.execute(query, (rid, tid))
        result = cursor.fetchone()
        return result

    def getTransactionDetailsByRidPurchasePriceAndQty(self, rid, purchaseprice, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where rid = %s and purchaseprice = %s and qty = %s;"
        cursor.execute(query, (rid, purchaseprice, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsByTidPurchasePriceAndQty(self, tid, purchaseprice, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where tid = %s and purchaseprice = %s and qty = %s;"
        cursor.execute(query, (tid, purchaseprice, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsByRidAndPurchasePrice(self, rid, purchaseprice):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where rid = %s and purchaseprice = %s;"
        cursor.execute(query, (rid, purchaseprice))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsByTidAndPurchasePrice(self, tid, purchaseprice):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where tid = %s and purchaseprice = %s;"
        cursor.execute(query, (tid, purchaseprice))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsByRidAndQty(self, rid, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where rid = %s and qty = %s;"
        cursor.execute(query, (rid, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsByTidAndQty(self, tid, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where tid = %s and qty = %s;"
        cursor.execute(query, (tid, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsByPurchasePriceAndQty(self, purchaseprice, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where purchaseprice = %s and qty = %s;"
        cursor.execute(query, (purchaseprice, qty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsByRid(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsByTid(self, tid):
        cursor = self.conn.cursor()
        query = """
        select purchaseprice, qty, rid, rname, catid, catname
        from resourcetransactiondetail natural inner join resource natural inner join category
        where tid = %s;
        """
        cursor.execute(query, (tid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsByQty(self, qty):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where qty = %s;"
        cursor.execute(query, (qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionDetailsByPurchasePrice(self, purchaseprice):
        cursor = self.conn.cursor()
        query = "select * from resourcetransactiondetail where purchaseprice = %s;"
        cursor.execute(query, (purchaseprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result
