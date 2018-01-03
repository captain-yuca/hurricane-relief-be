# from config.dbconfig import pg_config
import psycopg2
class AddressesDAO:
    # def __init__(self):

        # connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        #                                                     pg_config['user'],
        #                                                     pg_config['passwd'])
        # self.conn = psycopg2._connect(connection_url)

    def getAllAddresses(self):
        # cursor = self.conn.cursor()
        # query = "select * from user;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)

        result = [(1,'some address','something','00725', 'San Juan', 'Puerto Rico', 'Bayamon'),
                   (2,'some address','something','00680', 'Mayaguez', 'Puerto Rico', 'Mayaguez')]
        return result

    def getAddressById(self, add_id):
        # cursor = self.conn.cursor()
        # query = "select * from parts where pid = %s;"
        # cursor.execute(query, (pid,))
        # result = cursor.fetchone()
        result =  (add_id,'some address','something','00680', 'Mayaguez', 'Puerto Rico', 'Mayaguez')
        return result
