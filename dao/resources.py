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
