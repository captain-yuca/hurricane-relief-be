from config.dbconfig import pg_config
import psycopg2
class SuppliersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select sid, uid, username, lname, fname, isAdmin from suppliers natural join users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getSupplierById(self, sid):
        cursor = self.conn.cursor()
        query = "select sid, uid, username, lname, fname, isAdmin from suppliers natural join users where sid= %s";
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result
