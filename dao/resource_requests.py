from config.dbconfig import pg_config
import psycopg2
class ResourceRequestsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from resourcerequests;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, req_id):
        cursor = self.conn.cursor()
        query = "select * from resourcerequests where req_id=%s;"
        cursor.execute(query, (req_id,))
        result = cursor.fetchone()
        return result
