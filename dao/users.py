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
        query = "select uid, username, lname, fname, email, phone, add_id  from appuser;" # TOOK OUT ISADMIN HERE -Kelvin
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, username, lname, fname, email, phone, add_id from appuser where uid= %s"; # GONNA LEAVE ISADMIN HERE FOR NOW -Kelvin
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUsersByParameters(self, args):

        cursor = self.conn.cursor()

        query ="select uid, username, lname, fname, email, phone, add_id from appuser where " # TOOK OUT ISADMIN HERE -Kelvin
        query+= "=%s AND ".join(args.keys())
        query+= "=%s"

        cursor.execute(query, tuple(args.values()))
        result=[]
        for row in cursor:
            result.append(row)
        return result

    def insert(self, username, lastname, firstname, password, email, phone, add_id):

        cursor = self.conn.cursor()
        query = "insert into appuser(username, lname, fname, password, email, phone, add_id) values (%s, %s, %s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (username, lastname, firstname, password, email, phone, add_id,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def update(self, uid, username, lastname, firstname, password, email, phone, add_id):

        cursor = self.conn.cursor()
        query = "update appuser set username = %s, lname = %s, fname = %s, password = %s, email = %s, phone = %s, add_id = %s where uid = %s;"
        cursor.execute(query, (username, lastname, firstname, password, email, phone, add_id, uid,))
        self.conn.commit()
        return uid

    def updateAdmin(self, uid, isAdmin):

        cursor = self.conn.cursor()
        query = "update appuser set isAdmin = %s where uid = %s;"
        cursor.execute(query, (isAdmin, uid,))
        self.conn.commit()
        return uid

    def count(self):

        cursor =self.conn.cursor()
        query = "select count(*) from appuser"
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    def getUserIdByPIID(self, pi_id):
        cursor = self.conn.cursor()
        query = "select uid from appuser natural inner join paymentinfo where pi_id= %s"; # GONNA LEAVE ISADMIN HERE FOR NOW -Kelvin
        cursor.execute(query, (pi_id,))
        result = cursor.fetchone()
        return result
