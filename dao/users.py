from config.dbconfig import url
import psycopg2
class UsersDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid, username, lname, fname, add_id  from appuser;" # TOOK OUT ISADMIN HERE -Kelvin
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, username, lname, fname, isAdmin, add_id from appuser where uid= %s"; # GONNA LEAVE ISADMIN HERE FOR NOW -Kelvin
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUsersByParameters(self, args):

        cursor = self.conn.cursor()

        query ="select uid, username, lname, fname, add_id from appuser where " # TOOK OUT ISADMIN HERE -Kelvin
        query+= "=%s AND ".join(args.keys())
        query+= "=%s"

        cursor.execute(query, tuple(args.values()))
        result=[]
        for row in cursor:
            result.append(row)
        return result

    def insert(self, username, lastname, firstname, password, add_id):

        cursor = self.conn.cursor()
        query = "insert into appuser(username, lname, fname, password, add_id) values (%s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (username, lastname, firstname, password, add_id,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid
