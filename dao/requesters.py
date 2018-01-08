from config.dbconfig import pg_config
import psycopg2
class RequestersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = "select nid, uid, username, lname, fname, isAdmin, add_id from requester natural join appuser;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getRequesterById(self, nid):
        cursor = self.conn.cursor()
        query = "select nid, uid, username, lname, fname, isAdmin, add_id from requester natural join appuser where nid= %s";
        cursor.execute(query, (nid,))
        result = cursor.fetchone()
        return result
