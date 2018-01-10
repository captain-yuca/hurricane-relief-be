from config.dbconfig import pg_config
import psycopg2

class ResourcesDAO:
    def __init__(self):

       connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])

       self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)

        return result

    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resource where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourcesByRname(self, rname):
        cursor = self.conn.cursor()
        query = "select * from resource where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCatId(self, catId):
        cursor = self.conn.cursor()
        if(catId == 1) or catId == 9:
            query = "select * from resource where catid in " \
                    "(select subcat_id from subcategory where parent_id = %s);"
        else:
            query = "select * from resource where catid = %s;"
        cursor.execute(query, (catId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRnameAndCatId(self, rname, catId):
        cursor = self.conn.cursor()
        if (catId == 1) or catId == 9:
            query = "select * from resource where rname = %s and catid in" \
                    "(select subcat_id from subcategory where parent_id = %s);"
        else:
            query = "select * from resource where rname = %s and catid = %s;"
        cursor.execute(query, (rname, catId))
        result = []
        for row in cursor:
            result.append(row)
        return result
    #added by Herbert. supposed to implement 14
    def getResourcesBySupplier(self, supplier):
        cursor = self.conn.cursor()
        query = """
        select * from resource where rid in
        (select rid from supplier natural inner join appuser natural inner join stock natural inner join resource where sid in
        (select sid from supplier natural inner join appuser where username = %s));
        """
        cursor.execute(query, (supplier,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    #added by Herbert o satisfy Manuel point of get Resources from a request
    def getResourcesByRequest(self, req_id):
        cursor = self.conn.cursor()
        query = """
        select distinct * from resource where rid in
        (select rid from resourcerequestdetail where req_id = %s);
        """
        cursor.execute(query, (req_id,))
        result= []
        for row in cursor:
            result.append(row)
        return result
    # also added cause I though coudl be useful. Herbert!
    def getResourcesByNID(self, nid):
        cursor = self.conn.cursor()
        query = """
        select * from resource where rid in
        (select rid from resourcerequestdetail where req_id in
        (select req_id from resourcerequest where nid = %s ));
        """
        cursor.execute(query, (nid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    #also added by Herbert! evolution of the previous one
    def getResourcesByRequester(self, requester):
        cursor = self.conn.cursor()
        query = """
         select distinct * from resource where rid in
        (select rid from resourcerequestdetail where req_id in
        (select req_id from resourcerequest where nid in
        (select nid from appuser natural inner join requester where username = %s
        )));
        """
        cursor.execute(query,(requester,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    #also added by Herbert, this one seems VERy important
    def getResourcesByCategory(self, category):
        cursor = self.conn.cursor()

        if (category == 'water') or category == 'fuel':
            query = """
            select distinct * from resource where catid in
            (select subcat_id from subcategory where parent_id in
            (select catid from category where catname = %s));
            """
        else:
            query = """
            select * from resource where catid in
            (select catid from category where catname = %s);
            """
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getResourcesByStockParams(self, args, max_args, min_args):
        cursor = self.conn.cursor()


        query ="""
        select rid, rname, catid
        from supplier natural inner join appuser natural inner join stock natural inner join resource natural inner join category natural inner join address
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
