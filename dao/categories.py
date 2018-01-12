from config.dbconfig import url
import psycopg2

class CategoriesDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )
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
