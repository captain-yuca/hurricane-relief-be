from config.dbconfig import pg_config
import psycopg2
class AvailabilityAnnouncementsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAnnouncements(self):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncement;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementById(self, add_id):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncement where ann_id=%s;"
        cursor.execute(query, (add_id,))
        result = cursor.fetchone()
        return result
