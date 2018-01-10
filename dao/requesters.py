from config.dbconfig import pg_config
import psycopg2
class RequestersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect('postgres://ebwyoylyofgguf:bce5e728f4d5504e7a83ba37ece6f608483572bb56baa5700c90dab37d151295@ec2-54-83-59-144.compute-1.amazonaws.com:5432/de320ggpcvnl39')

    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = "select nid, uid, username, lname, fname, add_id from requester natural join appuser;" #Eliminated isAdmin parameter from query
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getRequesterById(self, nid):
        cursor = self.conn.cursor()
        query = "select nid, uid, username, lname, fname, add_id from requester natural join appuser where nid= %s"; #Eliminated isAdmin paramter from query -Kelvin
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
