# from config.dbconfig import pg_config
import psycopg2
class UsersDAO:
    # def __init__(self):

        # connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        #                                                     pg_config['user'],
        #                                                     pg_config['passwd'])
        # self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        # cursor = self.conn.cursor()
        # query = "select * from user;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)

        result = [(1,'captain','Manuel','Baez',True),
                   (2,'crayola','Jackelyn','Ivette',False)]
        return result
