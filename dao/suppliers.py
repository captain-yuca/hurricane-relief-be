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
        query = "select sid, uid, username, lname, fname, isAdmin, add_id from supplier natural join appuser;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getSupplierById(self, sid):
        cursor = self.conn.cursor()
        query = "select sid, uid, username, lname, fname, isAdmin, add_id from supplier natural join appuser where sid= %s";
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result


    def getSuppliersByResourceParams(self, args, max_args, min_args):

        cursor = self.conn.cursor()


        query ="""
        select sid, uid, username, lname, fname,  isadmin, add_id, currentpriceperitem, qtysum, rid, rname, catid, catname
        from supplier natural join appuser natural join stock natural join resource natural join category
        where
        """

        selection_length = len(args) + len(max_args) + len(min_args)

        i = 0

        # Go through each args list and append the key with its appropiate operator
        # and value. 'i' keeps track of when to stop appending AND.
        for key in min_args.keys():
            if i == selection_length - 1:
                query+= key + " < %s"
            else:
                query+= key + " < %s AND "
                i+=1
        for key in max_args.keys():
            if i == selection_length - 1:
                query+= key + " >= %s"
            else:
                query+= key + " >= %s AND "
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
            print(row)
            result.append(row)
        return result
