#from config.dbconfig import pg_config
import psycopg2

class ResourceTransactionsDAO:
    #def __init__(self):

        #connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pgconfig['passwd'])

        #self.conn = psycopg2._connect(connection_url)

    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "select * from resourceTransactions;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionById(self, tid):
        cursor = self.conn.cursor()
        query = "select * from resourceTransaction where tid = %s;"
        cursor.execute(query, (tid,))
        result = cursor.fetchone()
        return result

    def getTransactionsBySid(self, sid):
        cursor = self.conn.cursor()
        query = "select * from resourceTransaction where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByPurchaseid(self, purchaseid):
        cursor = self.conn.cursor()
        query = "select * from resourceTransaction where purchaseid = %s;"
        cursor.execute(query, (purchaseid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionBySidAndPurchaseId(self, sid, purchaseid):
        cursor = self.conn.cursor()
        query = "select * from resourceTransaction where sid = %s and purchaseid = %s;"
        cursor.execute(query, (sid, purchaseid))
        result = []
        for row in cursor:
            result.append(row)
        return result