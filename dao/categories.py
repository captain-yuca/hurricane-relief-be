from config.dbconfig import pg_config
import psycopg2

class CategoriesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])

        self.conn = psycopg2._connect('postgres://ebwyoylyofgguf:bce5e728f4d5504e7a83ba37ece6f608483572bb56baa5700c90dab37d151295@ec2-54-83-59-144.compute-1.amazonaws.com:5432/de320ggpcvnl39')

    def getAllCategories(self):
        cursor = self.conn.cursor()
        query = "select * from category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryById(self, catId):
        cursor = self.conn.cursor()
        query = "select * from category where catId = %s;"
        cursor.execute(query, (catId,))
        result = cursor.fetchone()
        return result

    def getCategoriesByName(self, catName):
        cursor = self.conn.cursor()
        if (catName == "water") or catName == "fuel":
            query = "select * from category where catid in " \
                    "(select subcat_id from subcategory where parent_id = " \
                    "(select catid from category where catName = %s));"
        else:
            query = "select * from category where catName = %s"
        cursor.execute(query, (catName,))
        result = []
        for row in cursor:
            result.append(row)
        return result
