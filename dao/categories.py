from config.dbconfig import pg_config
import psycopg2

class CategoriesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllCategories(self):
        cursor = self.conn.cursor()
        query = "select * from categories;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryById(self, catId):
        cursor = self.conn.cursor()
        query = "select * from categories where catId = %s;"
        cursor.execute(query, (catId,))
        result = cursor.fetchone()
        return result

    def getCategoriesByName(self, catName):
        cursor = self.conn.cursor()
        if (catName == "water") or catName == "fuel":
            query = "select * from categories where catid in " \
                    "(select subcat_id from subcategories where parent_id = " \
                    "(select catid from categories where catName = %s));"
        else:
            query = "select * from categories where catName = %s"
        cursor.execute(query, (catName,))
        result = []
        for row in cursor:
            result.append(row)
        return result
