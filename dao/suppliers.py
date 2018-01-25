from config.dbconfig import url
import psycopg2
class SuppliersDAO:
    def __init__(self):

        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select sid, uid, username, lname, fname, email, phone, add_id from supplier natural join appuser;" # Eliminated the isAdmin projection from this query -Kelvin
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getSupplierById(self, sid):
        cursor = self.conn.cursor()
        query = "select sid, uid, username, lname, fname, email, phone, add_id from supplier natural join appuser where sid= %s"; #Elmininated the isAdmin projection from this query -Kelvin
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result


    def getSuppliersByResourceParams(self, args, max_args, min_args):

        cursor = self.conn.cursor()

        # Eliminated the isAdmin projection from this option -Kelvin
        query ="""
        select distinct sid, uid, username, lname, fname, email, phone, add_id
        from supplier natural join appuser natural join stock natural join resource natural join category natural join address
        where
        """

        selection_length = len(args) + len(max_args) + len(min_args)

        i = 0

        # Go through each args list (args, max_args, min_args) and append the key with its appropiate operator
        # and value. 'i' keeps track of when to stop appending AND to the query.
        for key in min_args.keys():
            if i == selection_length - 1:
                query+= key + " >= %s"
            else:
                query+= key + " >= %s AND "
                i+=1
        for key in max_args.keys():
            if i == selection_length - 1:
                query+= key + " < %s"
            else:
                query+= key + " < %s AND "
                i+=1
        for key in args.keys():
            if i == selection_length - 1:
                query+= key + " = %s"
            else:
                query+= key + " = %s AND "
                i+=1

        args_tuple = tuple(min_args.values()) + tuple(max_args.values()) + tuple(args.values())
        cursor.execute(query, args_tuple)
        result=[]
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersCountPerRegion(self):
        cursor = self.conn.cursor()
        query = "select distinct count(*), region from address natural inner join appuser natural inner join supplier group by region;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    def insert(self, uid):

        cursor = self.conn.cursor()
        query = "insert into supplier(uid) values (%s) returning sid;"
        cursor.execute(query, (uid,))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid

    def count(self):

        cursor =self.conn.cursor()
        query = "select count(*) from supplier"
        cursor.execute(query)
        result = cursor.fetchone()
        return result
