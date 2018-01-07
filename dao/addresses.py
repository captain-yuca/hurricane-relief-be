from config.dbconfig import pg_config
import psycopg2
class AddressesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAddresses(self):
        cursor = self.conn.cursor()
        query = "select * from address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)


        return result

    def getAddressById(self, add_id):
        cursor = self.conn.cursor()
        query = "select * from address where add_id=%s;"
        cursor.execute(query, (add_id,))
        result = cursor.fetchone()
        return result

    def getAddressesByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select add_id, address1, address2, city, country, region, zipcode from user natural join address where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
