from config.dbconfig import url
import psycopg2
class AddressesDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )
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
        query = "select add_id, address1, address2, zipcode, region, country, city from appuser natural join address where uid = %s;"
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

    def insert(self, address1, address2, zipcode, region, country, city):
        cursor = self.conn.cursor()
        query = "insert into address(address1, address2, city, country, region, zipcode) values(%s, %s, %s, %s, %s, %s) returning add_id;"
        cursor.execute(query, (address1, address2, city, country, region, zipcode,))
        add_id = cursor.fetchone()[0]
        self.conn.commit()
        return add_id
