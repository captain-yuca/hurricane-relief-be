from config.dbconfig import pg_config
import psycopg2
class PaymentInfoDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

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
        query = "select * from paymentinfo where billing_pi_id=%s;"
        cursor.execute(query, (pi_id,))
        result = cursor.fetchone()
        return result
