from config.dbconfig import pg_config
import psycopg2
class UsersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect('postgres://ebwyoylyofgguf:bce5e728f4d5504e7a83ba37ece6f608483572bb56baa5700c90dab37d151295@ec2-54-83-59-144.compute-1.amazonaws.com:5432/de320ggpcvnl39')


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
