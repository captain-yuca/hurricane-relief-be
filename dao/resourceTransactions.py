from config.dbconfig import url
import psycopg2

class ResourceTransactionsDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )

    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "select tid, transactionammount, purchase_id, supplier_pi_id from resourcetransaction;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionById(self, tid):
        cursor = self.conn.cursor()
        query = """
        select tid, transactionammount, purchase_id, sid, uid, username, lname, fname, email, phone, add_id, qty, purchaseprice, rid, rname, catid, catname
        from resourcetransaction natural inner join resourcetransactiondetail natural inner join supplier natural inner join appuser natural inner join resource natural inner join category
        where tid=%s
        """
        cursor.execute(query, (tid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySid(self, sid):
        cursor = self.conn.cursor()
        query = "select tid, transactionammount, sid, supplier_pi_id, purchase_id from resourcetransaction where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByPurchaseid(self, purchaseid):
        cursor = self.conn.cursor()
        query = """
        select tid, transactionammount, sid, qty, purchaseprice, rid, rname, catid, catname
        from resourcetransaction natural inner join resourcetransactiondetail natural inner join resource natural inner join category
        where purchase_id = %s;
        """
        cursor.execute(query, (purchaseid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByPaymentInfoId(self, supplier_pi_id):
        cursor = self.conn.cursor()
        query = "select * from resourcetransaction where supplier_pi_id = %s;"
        cursor.execute(query, (supplier_pi_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionBySidAndPurchaseId(self, sid, purchaseid):
        cursor = self.conn.cursor()
        query = "select * from resourcetransaction where sid = %s and purchase_id = %s;"
        cursor.execute(query, (sid, purchaseid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySidAndPaymentInfoId(self, sid, supplier_pi_id):
        cursor = self.conn.cursor()
        query = "select * from resourcetransaction where sid = %s and supplier_pi_id = %s;"
        cursor.execute(query, (sid, supplier_pi_id))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getTransactionsByTransactionAmountAndPaymentInfoId(self, transaction_amount, supplier_pi_id):
        cursor = self.conn.cursor()
        query = "select * from resourcetransaction where transaction_amount = %s and supplier_pi_id = %s;"
        cursor.execute(query, (transaction_amount, supplier_pi_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySidPurchaseidTransactionAmount(self, sid, purchaseid, transaction_amount):
        cursor = self.conn.cursor()
        query = "select * from resourcetransaction where sid = %s and purchase_id = %s and transaction_amount = %s;"
        cursor.execute(query, (sid, purchaseid, transaction_amount))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySidAndTransactionAmount(self, sid, transaction_amount):
        cursor = self.conn.cursor()
        query = "select * from resourcetransaction where sid = %s and transaction_amount = %s;"
        cursor.execute(query, (sid, transaction_amount))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByPurchaseIdAndTransactionAmount(self, purchaseid, transaction_amount):
        cursor = self.conn.cursor()
        query = "select * from resourcetransaction where purchase_id = %s and transactionAmount = %s;"
        cursor.execute(query, (purchaseid, transaction_amount))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByTransactionAmount(self, transaction_amount):
        cursor = self.conn.cursor()
        query = "select * from resourcetransaction where transaction_amount = %s;"
        cursor.execute(query, (transaction_amount,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, sid, transactionammount, purchase_id, supplier_pi_id):
        cursor = self.conn.cursor()
        query = "insert into resourcetransaction(sid, transactionammount, purchase_id, supplier_pi_id) values (%s, %s, %s, %s) returning tid;"
        cursor.execute(query, (sid, transactionammount, purchase_id, supplier_pi_id,))
        uid = cursor.fetchone()
        self.conn.commit()
        return uid

    def updateTransactionAmmount(self, tid, transactionammount):
        cursor = self.conn.cursor()
        query = "update resourcetransaction set transactionammount = %s where tid = %s;"
        cursor.execute(query, (transactionammount, tid,))
        self.conn.commit()
