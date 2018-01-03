#from config.dbconfig import pg_config
import psycopg2

class ResourcesDAO:
    #def __init__(self):

     #   connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])

      #  self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)

        #result = [(1, 'Dasani', 1), (2, 'Diesel Puma', 3)]
        return result

    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourcesByRname(self, rname):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCatId(self, catId):
        cursor = self.conn.cursor()
        if(catId == 1) or catId == 9:
            query = "select * from resources where catid in " \
                    "(select subcat_id from subcategories where parent_id = %s);"
        else:
            query = "select * from resources where catid = %s;"
        cursor.execute(query, (catId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRnameAndCatId(self, rname, catId):
        cursor = self.conn.cursor()
        if (catId == 1) or catId == 9:
            query = "select * from resources where rname = %s and catid in" \
                    "(select subcat_id from subcategories where parent_id = %s);"
        else:
            query = "select * from resources where rname = %s and catid = %s;"
        cursor.execute(query, (rname, catId))
        result = []
        for row in cursor:
            result.append(row)
        return result


