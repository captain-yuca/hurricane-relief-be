from config.dbconfig import url
import psycopg2
class PaymentInfoDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )
    def getAllPaymentInfo(self):
        cursor = self.conn.cursor()
        query = "select * from paymentinfo;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getPaymentInfoByUID(self, uid):
        cursor = self.conn.cursor()
        query = "select * from paymentinfo where uid=%s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)

        return result
    def getPaymentInfoById(self, pi_id):
        cursor = self.conn.cursor()
        query = "select pi_id, ccnum, expirationDate, add_id from paymentinfo where pi_id=%s;"
        cursor.execute(query, (pi_id,))
        result = cursor.fetchone()
        return result

    def getPaymentInfoBySid(self, sid):
        cursor = self.conn.cursor()
        query = "select pi_id from paymentinfo natural inner join appuser natural inner join supplier where sid=%s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getPaymentInfoByCCNum(self, ccNum):
        cursor = self.conn.cursor()
        query = "select pi_id from paymentinfo natural inner join appuser natural inner join supplier where ccnum=%s;"
        cursor.execute(query, (ccNum,))
        result = cursor.fetchone()
        return result


    def insertPaymentInfo(self, ccNum, expirationDate, uid, add_id):
        cursor = self.conn.cursor()
        query = "insert into PaymentInfo(ccNum, expirationDate, uid, add_id) values (%s,%s,%s,%s) returning pi_id;"
        cursor.execute(query, (ccNum, expirationDate, uid, add_id,))
        pi_id = cursor.fetchone()[0]
        self.conn.commit()
        return pi_id
