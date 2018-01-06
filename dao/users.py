from config.dbconfig import pg_config
import psycopg2
class UsersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid, username, lname, fname, isAdmin from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, username, lname, fname, isAdmin from users where uid= %s";
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUsersByParameters(self, args):

        cursor = self.conn.cursor()

        query ="select uid, username, lname, fname, isAdmin from users where "
        query+= "=%s AND ".join(args.keys())
        query+= "=%s"

        cursor.execute(query, tuple(args.values()))
        result=[]
        for row in cursor:
            result.append(row)
        return result
