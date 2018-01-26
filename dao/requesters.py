from config.dbconfig import url
import psycopg2
class RequestersDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )
    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = "select nid, uid, username, lname, fname, email, phone, add_id from requester natural join appuser;" #Eliminated isAdmin parameter from query
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getRequesterById(self, nid):
        cursor = self.conn.cursor()
        query = "select nid, uid, username, lname, fname, email, phone, add_id from requester natural join appuser where nid= %s"; #Eliminated isAdmin paramter from query -Kelvin
        cursor.execute(query, (nid,))
        result = cursor.fetchone()
        return result

    def getRequestersCountByRegion(self):
        cursor = self.conn.cursor()
        query = "select count(*), region from address natural inner join user natural inner join requester group by region;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, uid):
        cursor = self.conn.cursor()
        query = "insert into requester(uid) values(%s) returning nid;"
        cursor.execute(query, (uid,))
        nid = cursor.fetchone()[0]
        self.conn.commit()
        return nid
