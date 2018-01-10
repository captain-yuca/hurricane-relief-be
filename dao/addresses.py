from config.dbconfig import pg_config
import psycopg2
class AddressesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect('postgres://ebwyoylyofgguf:bce5e728f4d5504e7a83ba37ece6f608483572bb56baa5700c90dab37d151295@ec2-54-83-59-144.compute-1.amazonaws.com:5432/de320ggpcvnl39')

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
        query = "select add_id, address1, address2, city, country, region, zipcode from appuser natural join address where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressBySid(self, sid):
        cursor = self.conn.cursor()
        query = "select add_id, address1, address2, city, country, region, zipcode from appuser natural join address where uid = " \
                "(select uid from supplier where sid = %s);"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result
