from config.dbconfig import pg_config
import psycopg2

class PurchaseDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect('postgres://ebwyoylyofgguf:bce5e728f4d5504e7a83ba37ece6f608483572bb56baa5700c90dab37d151295@ec2-54-83-59-144.compute-1.amazonaws.com:5432/de320ggpcvnl39')

    def getAllPurchases(self):
        cursor = self.conn.cursor()
        query = "select * from purchase;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchaseById(self, purchase_id):
        cursor = self.conn.cursor()
        query = """
        select purchase_id, purchase_date, purchase_total, appuser.uid, username, lname, fname, appuser.add_id, pi_id, ccnum, expirationdate, paymentinfo.add_id, tid, sid, transactionammount
        from (purchase natural inner join resourcetransaction natural inner join appuser),address, paymentinfo
        where address.add_id = paymentinfo.add_id and paymentinfo.pi_id = purchase.buyer_pi_id and purchase_id = %s;
        """
        cursor.execute(query, (purchase_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByDateTotalUidAndBuyerPaymentInfoId(self, date, total, uid, buyer_pi_id):
        cursor = self.conn.cursor()
        query = "select * from purchase where purchase_date = %s " \
                "and purchase_total = %s and uid = %s and buyer_pi_id = %s;"
        cursor.execute(query, (date, total, uid, buyer_pi_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByDateTotalAndUid(self, date, total, uid):
        cursor = self.conn.cursor()
        query = "select * from purchase where purchase_date = %s and purchase_total = %s and uid = %s;"
        cursor.execute(query, (date, total, uid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByDateTotalAndBuyerPaymentInfoId(self, date, total, buyer_pi_id):
        cursor = self.conn.cursor()
        query = "select * from purchase where purchase_date = %s and purchase_total = %s and buyer_pi_id = %s;"
        cursor.execute(query, (date, total, buyer_pi_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByTotalUidAndBuyerPaymentInfoId(self, total, uid, buyer_pi_id):
        cursor = self.conn.cursor()
        query = "select * from purchase where purchase_total = %s and uid = %s and buyer_pi_id = %s;"
        cursor.execute(query, (total, uid, buyer_pi_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByDateUidAndBuyerPaymentInfoId(self, date, uid, buyer_pi_id):
        cursor = self.conn.cursor()
        query = "select * from purchase where purchase_date = %s and uid = %s and buyer_pi_id = %s;"
        cursor.execute(query, (date, uid, buyer_pi_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByDateAndTotal(self, date, total):
        cursor = self.conn.cursor()
        query = "select * from purchase where purchase_date = %s " \
                "and purchase_total = %s;"
        cursor.execute(query, (date, total))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByDateAndUid(self, date, uid):
        cursor = self.conn.cursor()
        query = "select * from purchase where purchase_date = %s " \
                "and uid = %s;"
        cursor.execute(query, (date, uid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByDateAndBuyerPaymentInfo(self, date, buyer_pi_id):
        cursor = self.conn.cursor()
        query = "select * from purchase where purchase_date = %s " \
                "and buyer_pi_id = %s;"
        cursor.execute(query, (date, buyer_pi_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByTotalAndUid(self, total, uid):
        cursor = self.conn.cursor()
        query = "select * from purchase where" \
                "purchase_total = %s and uid = %s;"
        cursor.execute(query, (total, uid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByTotalAndBuyerPaymentInfoId(self, total, buyer_pi_id):
        cursor = self.conn.cursor()
        query = "select * from purchase where " \
                "purchase_total = %s and buyer_pi_id = %s;"
        cursor.execute(query, (total, buyer_pi_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByUidAndBuyerPaymentInfoId(self, uid, buyer_pi_id):
        cursor = self.conn.cursor()
        query = "select * from purchase where " \
                "uid = %s and buyer_pi_id = %s;"
        cursor.execute(query, (uid, buyer_pi_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByDate(self, date):
        cursor = self.conn.cursor()
        query = "select * from purchase where purchase_date = %s;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByTotal(self, total):
        cursor = self.conn.cursor()
        query = "select * from purchase where " \
                "purchase_total = %s;"
        cursor.execute(query, (total,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByUid(self, uid):
        cursor = self.conn.cursor()
        query = """
        select purchase_id, purchase_date, purchase_total, purchase.uid, pi_id, ccnum, expirationdate
        from purchase inner join paymentinfo on purchase.buyer_pi_id = paymentinfo.pi_id
        where purchase.uid = %s;
        """
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByBuyerPaymentInfoId(self, buyer_pi_id):
        cursor = self.conn.cursor()
        query = "select * from purchase where" \
                "buyer_pi_id = %s;"
        cursor.execute(query, (buyer_pi_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    #added by Herbert, supposed to implement 18
    def getPurchasesBySupplier(self, username):
        cursor = self.conn.cursor()
        query=  """
                select purchase_id, tid,  rname, catname, purchaseprice, transactionammount, purchase_date
                from purchase natural inner join resourcetransaction natural inner join resourcetransactiondetail natural inner join resource natural inner join category
                where sid in
                (select sid from appuser natural inner join supplier
                where username= %s );
                """
        cursor.execute(query, (username,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getAllReserves(self):
        cursor = self.conn.cursor()
        query=  """
                select purchase.purchase_id, tid,  rname, catname, purchaseprice, transactionammount, purchase_date, s_user.username as supplier, u_user.username as buyer
                from (resourcetransaction natural inner join resourcetransactiondetail natural inner join resource natural inner join category), appuser as s_user, appuser as u_user, purchase, supplier
                where (s_user.uid=supplier.uid) and (u_user.uid=purchase.uid) AND (purchase.purchase_id=resourcetransaction.purchase_id) and purchaseprice=0;
                """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllPaidPurchases(self):
        cursor = self.conn.cursor()
        query = """
                select purchase.purchase_id, tid,  rname, catname, purchaseprice, transactionammount, purchase_date, s_user.username as supplier, u_user.username as buyer
                from (resourcetransaction natural inner join resourcetransactiondetail natural inner join resource natural inner join category), appuser as s_user, appuser as u_user, purchase, supplier
                where (s_user.uid=supplier.uid) and (u_user.uid=purchase.uid) AND (purchase.purchase_id=resourcetransaction.purchase_id) and purchaseprice>0;
                """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
