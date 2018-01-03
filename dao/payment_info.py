# from config.dbconfig import pg_config
import psycopg2
class PaymentInfoDAO:
    # def __init__(self):

        # connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        #                                                     pg_config['user'],
        #                                                     pg_config['passwd'])
        # self.conn = psycopg2._connect(connection_url)

    def getAllPaymentInfo(self):
        # cursor = self.conn.cursor()
        # query = "select * from user;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)

        result = [(1,'8888888888888888','2828-09-10'),
                   (2,'8888888888888888','2828-09-10')]
        return result

    def getPaymentInfoById(self, pi_id):
        # cursor = self.conn.cursor()
        # query = "select * from parts where pid = %s;"
        # cursor.execute(query, (pid,))
        # result = cursor.fetchone()
        result =  (pi_id,'8888888888888888','2828-09-10')
        return result
