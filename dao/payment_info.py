from config.dbconfig import pg_config
import psycopg2
class PaymentInfoDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect('postgres://ebwyoylyofgguf:bce5e728f4d5504e7a83ba37ece6f608483572bb56baa5700c90dab37d151295@ec2-54-83-59-144.compute-1.amazonaws.com:5432/de320ggpcvnl39')

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
