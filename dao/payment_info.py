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

    def getPaymentInfoById(self, pi_id):
        cursor = self.conn.cursor()
        query = "select * from paymentinfo where pi_id=%s;"
        cursor.execute(query, (pi_id,))
        result = cursor.fetchone()
        return result
